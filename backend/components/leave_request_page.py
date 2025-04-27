from PyQt5 import QtWidgets, QtCore
from utils import get_db_connection
from PyQt5.QtGui import QFont

class LeaveRequestPage(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QtWidgets.QVBoxLayout(self)

        # Title
        self.title = QtWidgets.QLabel("Pending Leave Requests")
        self.title.setStyleSheet("font-size: 20px; font-weight: bold; margin-bottom: 10px;")
        self.layout.addWidget(self.title)

        # ListWidget to show leave applications
        self.leave_list = QtWidgets.QListWidget()
        self.layout.addWidget(self.leave_list)

        # Load pending leaves
        self.load_pending_leaves()

        # Connect clicking an item
        self.leave_list.itemClicked.connect(self.open_leave_dialog)

    def load_pending_leaves(self):
        self.leave_list.clear()
        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)

            query = """
            SELECT 
                la.leaveapplication_id, 
                e.firstname, 
                e.lastname, 
                lt.name AS leave_type, 
                la.date, 
                la.reason
            FROM LeaveApplication la
            JOIN Employee e ON la.employee_id = e.employee_id
            JOIN LeaveType lt ON la.leavetype_id = lt.leavetype_id
            WHERE la.status = 'pending'
            """
            cursor.execute(query)
            results = cursor.fetchall()

            for leave in results:
                # Create a QWidget for each row
                item_widget = QtWidgets.QWidget()
                layout = QtWidgets.QHBoxLayout(item_widget)
                layout.setContentsMargins(10, 5, 10, 5)  # Margin inside each item
                layout.setSpacing(30)  # Space between columns

                # Create 3 labels
                name_label = QtWidgets.QLabel(f"{leave['firstname']} {leave['lastname']}")
                leave_type_label = QtWidgets.QLabel(f"{leave['leave_type'].capitalize()} Leave")
                date_label = QtWidgets.QLabel(leave['date'].strftime("%B %d, %Y"))

                # Set font styles (bigger)
                font = QFont()
                font.setPointSize(12)
                name_label.setFont(font)
                leave_type_label.setFont(font)
                date_label.setFont(font)

                # Stretch policy to balance columns
                name_label.setMinimumWidth(250)
                leave_type_label.setMinimumWidth(200)
                date_label.setMinimumWidth(150)

                # Add labels into the layout
                layout.addWidget(name_label)
                layout.addWidget(leave_type_label)
                layout.addWidget(date_label)

                # Create QListWidgetItem to hold this widget
                list_item = QtWidgets.QListWidgetItem(self.leave_list)
                list_item.setSizeHint(item_widget.sizeHint())  # Auto size height

                # Add to QListWidget
                self.leave_list.addItem(list_item)
                self.leave_list.setItemWidget(list_item, item_widget)

                # Store full leave data into item for later click
                list_item.setData(QtCore.Qt.UserRole, leave)

            cursor.close()
            conn.close()
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"Failed to load leaves: {e}")


    def open_leave_dialog(self, item):
        leave_data = item.data(QtCore.Qt.UserRole)

        dialog = QtWidgets.QDialog(self)
        dialog.setWindowTitle("Approve or Deny Leave")
        layout = QtWidgets.QVBoxLayout(dialog)

        info_label = QtWidgets.QLabel(
        f"Employee: {leave_data['firstname'].capitalize()} {leave_data['lastname'].capitalize()}\n"
        f"Leave Type: {leave_data['leave_type'].capitalize()}\n"
        f"Date: {leave_data['date']}\n"
        f"Reason: {leave_data['reason'].capitalize()}"
    )

        layout.addWidget(info_label)

        buttons_layout = QtWidgets.QHBoxLayout()

        approve_btn = QtWidgets.QPushButton("Approve")
        deny_btn = QtWidgets.QPushButton("Deny")

        buttons_layout.addWidget(approve_btn)
        buttons_layout.addWidget(deny_btn)

        layout.addLayout(buttons_layout)

        approve_btn.clicked.connect(lambda: self.approve_leave(leave_data, dialog))
        deny_btn.clicked.connect(lambda: self.deny_leave(leave_data, dialog))

        dialog.exec_()

    def approve_leave(self, leave_data, dialog):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            # 1. Update leave status
            cursor.execute(
                "UPDATE LeaveApplication SET status = 'approved' WHERE leaveapplication_id = %s",
                (leave_data['leaveapplication_id'],)
            )

            # 2. Deduct leave balance based on leave type
            if leave_data['leave_type'] == 'casual':
                cursor.execute(
                    "UPDATE Employee SET casualLeaves = casualLeaves - 1 WHERE firstname = %s AND lastname = %s",
                    (leave_data['firstname'], leave_data['lastname'])
                )
            elif leave_data['leave_type'] == 'sick':
                cursor.execute(
                    "UPDATE Employee SET sickLeaves = sickLeaves - 1 WHERE firstname = %s AND lastname = %s",
                    (leave_data['firstname'], leave_data['lastname'])
                )
            elif leave_data['leave_type'] == 'paid':
                cursor.execute(
                    "UPDATE Employee SET paidLeaves = paidLeaves - 1 WHERE firstname = %s AND lastname = %s",
                    (leave_data['firstname'], leave_data['lastname'])
                )

            conn.commit()
            cursor.close()
            conn.close()

            QtWidgets.QMessageBox.information(self, "Success", "Leave Approved Successfully!")
            dialog.accept()
            self.load_pending_leaves()  # Refresh list
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"Failed to approve leave: {e}")

    def deny_leave(self, leave_data, dialog):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                "UPDATE LeaveApplication SET status = 'denied' WHERE leaveapplication_id = %s",
                (leave_data['leaveapplication_id'],)
            )

            conn.commit()
            cursor.close()
            conn.close()

            QtWidgets.QMessageBox.information(self, "Success", "Leave Denied Successfully!")
            dialog.accept()
            self.load_pending_leaves()
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"Failed to deny leave: {e}")

def show_leave_request(self):
    page = LeaveRequestPage(self)
    self.ui.dashboardStackedWidget.addWidget(page)
    self.ui.dashboardStackedWidget.setCurrentWidget(page)
    