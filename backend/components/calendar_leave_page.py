# calendar_leave_page.py
from utils import get_db_connection
from PyQt5 import QtWidgets, QtCore, QtGui

def show_calendar_leave(self):
    self.ui.dashboardStackedWidget.setCurrentWidget(self.ui.calendarLeavePage)

    # Connect calendar click event immediately
    self.ui.calendarWidget.clicked.connect(lambda date: show_employees_on_date(self, date))

    # Highlight dates with approved leaves
    load_calendar_data(self)

def load_calendar_data(self):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        query = """
            SELECT date
            FROM LeaveApplication
            WHERE status = 'approved'
        """
        cursor.execute(query)
        results = cursor.fetchall()

        format = QtGui.QTextCharFormat()
        format.setBackground(QtGui.QBrush(QtGui.QColor("red")))
        format.setForeground(QtGui.QBrush(QtGui.QColor("white")))
        format.setFontWeight(QtGui.QFont.Bold)

        for entry in results:
            date = entry['date']
            date_obj = QtCore.QDate(date.year, date.month, date.day)
            self.ui.calendarWidget.setDateTextFormat(date_obj, format)

        cursor.close()
        conn.close()

    except Exception as e:
        print(f"[ERROR] Loading calendar highlights: {e}")

def show_employees_on_date(self, qdate):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        date_str = qdate.toString("yyyy-MM-dd")

        query = """
            SELECT e.firstname, e.lastname, la.reason
            FROM LeaveApplication la
            JOIN Employee e ON la.employee_id = e.employee_id
            WHERE la.date = %s AND la.status = 'approved'
        """
        cursor.execute(query, (date_str,))
        employees = cursor.fetchall()

        cursor.close()
        conn.close()

        if not employees:
            QtWidgets.QMessageBox.information(self, "No Leaves", "No approved leaves on this date.")
            return

        # Create a popup dialog
        dialog = QtWidgets.QDialog(self)
        dialog.setWindowTitle(f"Approved Leaves - {qdate.toString('MMMM d, yyyy')}")
        dialog.setFixedSize(400, 400)

        layout = QtWidgets.QVBoxLayout(dialog)

        for emp in employees:
            fullname = f"{emp['firstname']} {emp['lastname']}"
            reason = emp['reason']

            label = QtWidgets.QLabel(f"<b>{fullname}</b><br>Reason: {reason}")
            label.setWordWrap(True)
            layout.addWidget(label)

        close_btn = QtWidgets.QPushButton("Close")
        close_btn.clicked.connect(dialog.accept)
        layout.addWidget(close_btn)

        dialog.exec_()

    except Exception as e:
        print(f"[ERROR] Showing employees in dialog: {e}")
