from utils import get_db_connection
from PyQt5 import QtWidgets, QtCore, QtGui

def show_dashboard(self):
    self.ui.dashboardStackedWidget.setCurrentWidget(self.ui.dashboardPage)

    # Initialize pagination state if not already present
    if not hasattr(self, 'leave_page'):
        self.leave_page = 0
    if not hasattr(self, 'leaves_per_page'):
        self.leaves_per_page = 10

    def load_statistics():
        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)

            cursor.execute("""
                SELECT 
                    SUM(casualLeaves + sickLeaves + paidLeaves) AS total_leaves,
                    SUM(casualLeaves) AS total_casual,
                    SUM(sickLeaves) AS total_sick,
                    SUM(paidLeaves) AS total_paid
                FROM Employee
            """)
            result = cursor.fetchone()
            print(f"[DASHBOARD] Statistics: {result}")

            if result:
                self.ui.totalLeaveLabel.setText(f"<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:600;\">{result['total_leaves'] or 0}</span></p></body></html>")
                self.ui.TotalCasualLeaveLabel.setText(f"<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:600;\">{result['total_casual'] or 0}</span></p></body></html>")
                self.ui.totalSickLeaveLabel.setText(f"<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:600;\">{result['total_sick'] or 0}</span></p></body></html>")
                self.ui.totalPaidEarnedLeaveLabel.setText(f"<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:600;\">{result['total_paid'] or 0}</span></p></body></html>")
            else:
                print("[DASHBOARD] No statistics found.")

            cursor.close()
            conn.close()
        except Exception as e:
            print(f"[ERROR] Dashboard Statistics Failed: {e}")
            QtWidgets.QMessageBox.critical(self, "Error", f"Failed to load statistics:\n{e}")

    def load_leave_data():
        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)

            # Total record count
            cursor.execute("SELECT COUNT(*) AS total FROM LeaveApplication")
            total = cursor.fetchone()['total']
            offset = self.leave_page * self.leaves_per_page

            cursor.execute("""
                SELECT 
                    e.firstname,
                    e.lastname,
                    lt.name AS leave_type,
                    la.date,
                    la.status
                FROM LeaveApplication la
                JOIN Employee e ON la.employee_id = e.employee_id
                JOIN LeaveType lt ON la.leavetype_id = lt.leavetype_id
                ORDER BY la.date DESC
                LIMIT %s OFFSET %s
            """, (self.leaves_per_page, offset))
            recent_leaves = cursor.fetchall()

            self.ui.recentLeaveTable.setRowCount(0)
            self.ui.recentLeaveTable.setColumnCount(4)
            self.ui.recentLeaveTable.setHorizontalHeaderLabels(["Employee Name", "Leave Type", "Date", "Status"])
            self.ui.recentLeaveTable.horizontalHeader().setStretchLastSection(True)
            self.ui.recentLeaveTable.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

            for row_num, leave in enumerate(recent_leaves):
                self.ui.recentLeaveTable.insertRow(row_num)

                fullname = f"{leave['firstname']} {leave['lastname']}"
                self.ui.recentLeaveTable.setItem(row_num, 0, QtWidgets.QTableWidgetItem(fullname))
                self.ui.recentLeaveTable.setItem(row_num, 1, QtWidgets.QTableWidgetItem(leave['leave_type'].capitalize()))
                self.ui.recentLeaveTable.setItem(row_num, 2, QtWidgets.QTableWidgetItem(leave['date'].strftime("%B %d, %Y")))

                status_item = QtWidgets.QTableWidgetItem(leave['status'].capitalize())
                color = {'approved': 'green', 'pending': 'orange', 'denied': 'red'}.get(leave['status'], 'black')
                status_item.setForeground(QtGui.QBrush(QtGui.QColor(color)))
                status_item.setFont(QtGui.QFont("", weight=QtGui.QFont.Bold))
                self.ui.recentLeaveTable.setItem(row_num, 3, status_item)

            # Disable buttons as needed
            self.ui.leaveRequestTablePrevBTN.setEnabled(self.leave_page > 0)
            self.ui.leaveRequestTableNextBTN.setEnabled((self.leave_page + 1) * self.leaves_per_page < total)

            cursor.close()
            conn.close()

        except Exception as e:
            print(f"[ERROR] Leave Table Load Failed: {e}")
            QtWidgets.QMessageBox.critical(self, "Error", f"Failed to load leave data:\n{e}")

    # Prevent rebinding on every tab switch
    try:
        self.ui.leaveRequestTableNextBTN.clicked.disconnect()
        self.ui.leaveRequestTablePrevBTN.clicked.disconnect()
    except Exception:
        pass

    self.ui.leaveRequestTableNextBTN.clicked.connect(lambda: next_page())
    self.ui.leaveRequestTablePrevBTN.clicked.connect(lambda: prev_page())

    def next_page():
        self.leave_page += 1
        load_leave_data()

    def prev_page():
        if self.leave_page > 0:
            self.leave_page -= 1
        load_leave_data()

    # Load everything
    load_statistics()
    load_leave_data()
