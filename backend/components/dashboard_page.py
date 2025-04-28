from utils import get_db_connection
from PyQt5 import QtWidgets, QtCore, QtGui

def show_dashboard(self):
    self.ui.dashboardStackedWidget.setCurrentWidget(self.ui.dashboardPage)
    
    try:
        print("[DASHBOARD] Connecting to database to fetch statistics...")
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        # Fetch total available leaves
        cursor.execute("""
            SELECT 
                SUM(casualLeaves + sickLeaves + paidLeaves) AS total_leaves,
                SUM(casualLeaves) AS total_casual,
                SUM(sickLeaves) AS total_sick,
                SUM(paidLeaves) AS total_paid
            FROM Employee
        """)
        result = cursor.fetchone()
        print(f"[DASHBOARD] Query Result: {result}")

        if result:
            self.ui.totalLeaveLabel.setText(f"<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:600;\">{result['total_leaves'] or 0}</span></p></body></html>")
            self.ui.TotalCasualLeaveLabel.setText(f"<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:600;\">{result['total_casual'] or 0}</span></p></body></html>")
            self.ui.totalSickLeaveLabel.setText(f"<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:600;\">{result['total_sick'] or 0}</span></p></body></html>")
            self.ui.totalPaidEarnedLeaveLabel.setText(f"<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:600;\">{result['total_paid'] or 0}</span></p></body></html>")
        else:
            print("[DASHBOARD] No data found.")

        # NOW fetch recent leaves!
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
            LIMIT 10
        """)
        recent_leaves = cursor.fetchall()

        self.ui.recentLeaveTable.setRowCount(0)
        self.ui.recentLeaveTable.setColumnCount(4)
        self.ui.recentLeaveTable.setHorizontalHeaderLabels(["Employee Name", "Leave Type", "Date", "Status"])
        self.ui.recentLeaveTable.horizontalHeader().setStretchLastSection(True)
        self.ui.recentLeaveTable.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        for row_num, leave in enumerate(recent_leaves):
            self.ui.recentLeaveTable.insertRow(row_num)

            fullname = f"{leave['firstname']} {leave['lastname']}"
            name_item = QtWidgets.QTableWidgetItem(fullname)
            name_item.setFlags(QtCore.Qt.ItemIsEnabled)
            self.ui.recentLeaveTable.setItem(row_num, 0, name_item)

            leave_type_item = QtWidgets.QTableWidgetItem(leave['leave_type'].capitalize())
            leave_type_item.setFlags(QtCore.Qt.ItemIsEnabled)
            self.ui.recentLeaveTable.setItem(row_num, 1, leave_type_item)

            date_item = QtWidgets.QTableWidgetItem(leave['date'].strftime("%B %d, %Y"))
            date_item.setFlags(QtCore.Qt.ItemIsEnabled)
            self.ui.recentLeaveTable.setItem(row_num, 2, date_item)

            status_item = QtWidgets.QTableWidgetItem(leave['status'].capitalize())
            status_item.setFlags(QtCore.Qt.ItemIsEnabled)

            if leave['status'] == 'approved':
                status_item.setForeground(QtGui.QBrush(QtGui.QColor('green')))
                status_item.setFont(QtGui.QFont("", weight=QtGui.QFont.Bold))
            elif leave['status'] == 'pending':
                status_item.setForeground(QtGui.QBrush(QtGui.QColor('orange')))
                status_item.setFont(QtGui.QFont("", weight=QtGui.QFont.Bold))
            elif leave['status'] == 'denied':
                status_item.setForeground(QtGui.QBrush(QtGui.QColor('red')))
                status_item.setFont(QtGui.QFont("", weight=QtGui.QFont.Bold))

            self.ui.recentLeaveTable.setItem(row_num, 3, status_item)

        print("[DASHBOARD] Recent leave requests loaded into table.")

        cursor.close()
        conn.close()
        print("[DASHBOARD] Database connection closed.")

    except Exception as e:
        print(f"[ERROR] Dashboard Statistics Failed: {e}")
        QtWidgets.QMessageBox.critical(self, "Error", f"Failed to load dashboard statistics:\n{e}")
