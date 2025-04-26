from PyQt5 import QtWidgets, QtCore
from UI.memberDashboard import Ui_MemberMainWindow
from utils import get_db_connection
import datetime

class MemberMainDashboard(QtWidgets.QMainWindow):
    def __init__(self, welcome_window, employee_data):
        super().__init__()
        self.ui = Ui_MemberMainWindow()
        self.ui.setupUi(self)

        self.welcome_window = welcome_window
        self.employee_data = employee_data
        self.ui.memberStackedWidget.setCurrentWidget(self.ui.memberDashboard)

        self.update_dashboard()
        self.start_clock()

        # Navigation
        self.ui.memberDashboardBTN.clicked.connect(self.show_member_dashboard)
        self.ui.memberFileLeaveBTN.clicked.connect(self.show_member_file_leave)
        self.ui.memberNotificationBTN.clicked.connect(self.show_member_notification)
        self.ui.memberSettingsBTN.clicked.connect(self.show_member_settings)
        self.ui.memberLogoutBTN.clicked.connect(self.member_logout_process)

        # Calendar click
        self.ui.leaveRequestCalendar.clicked.connect(self.update_chosen_date)

        # Settings
        self.ui.settingsSaveBTN.clicked.connect(self.save_settings)
        self.ui.settingsEditBTN.clicked.connect(self.enable_edit_mode)

        # File a Leave
        self.ui.leaveRequestSubmitBTN.clicked.connect(self.submit_leave_application)
        self.ui.leaveRequestClearBTN.clicked.connect(self.clear_leave_form)

        # Disable editable fields initially
        self.set_account_fields_enabled(False)
        self.ui.leaveRequestName.setText(f"{self.employee_data['firstname']} {self.employee_data['middlename']} {self.employee_data['lastname']}")
        self.ui.leaveRequestName.setEnabled(False)

        self.populate_leave_types()

    def update_dashboard(self):
        full_name = f"{self.employee_data['firstname']} {self.employee_data['middlename']} {self.employee_data['lastname']}".strip()
        self.ui.dashboardUser.setText(f"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">{full_name}</span></p></body></html>")

        self.ui.dashboardSickLeaveLabel.setText(f"<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:600;\">{self.employee_data['sick_leaves']}</span></p></body></html>")
        self.ui.dashboardCasualLeaveLabel.setText(f"<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:600;\">{self.employee_data['casual_leaves']}</span></p></body></html>")
        self.ui.dashboardPaidLeaveLabel.setText(f"<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:600;\">{self.employee_data['paid_leaves']}</span></p></body></html>")

    def update_settings_tab(self):
        self.ui.settingsFirstname.setText(f"<b>First Name:</b> {self.employee_data['firstname']}")
        self.ui.settingsMiddlename.setText(f"<b>Middle Name:</b> {self.employee_data['middlename']}")
        self.ui.settingsLastname.setText(f"<b>Last Name:</b> {self.employee_data['lastname']}")
        self.ui.settingsSuffix.setText(f"<b>Suffix:</b> {self.employee_data['suffix'] or 'N/A'}")
        self.ui.settingsProvince.setText(f"<b>Province:</b> {self.employee_data['province']}")
        self.ui.settingsCity.setText(f"<b>City:</b> {self.employee_data['city']}")
        self.ui.settingsBarangay.setText(f"<b>Barangay:</b> {self.employee_data['baranggay']}")
        self.ui.settingsZipCode.setText(f"<b>Zip Code:</b> {self.employee_data['zipcode']}")

        self.ui.settingsUsername.setText(self.employee_data['username'])
        self.ui.settingsEmail.setText(self.employee_data['email'])
        self.ui.settingsPassword.setText(self.employee_data['password'])
        self.ui.settingsConfirmPassword.setText(self.employee_data['password'])

        self.ui.settingsPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ui.settingsConfirmPassword.setEchoMode(QtWidgets.QLineEdit.Password)

        self.set_account_fields_enabled(False)

    def set_account_fields_enabled(self, enabled):
        self.ui.settingsUsername.setEnabled(enabled)
        self.ui.settingsEmail.setEnabled(enabled)
        self.ui.settingsPassword.setEnabled(enabled)
        self.ui.settingsConfirmPassword.setEnabled(enabled)

    def enable_edit_mode(self):
        self.set_account_fields_enabled(True)

    def save_settings(self):
        username = self.ui.settingsUsername.text().strip()
        email = self.ui.settingsEmail.text().strip()
        password = self.ui.settingsPassword.text().strip()
        confirm_password = self.ui.settingsConfirmPassword.text().strip()

        if password != confirm_password:
            QtWidgets.QMessageBox.warning(self, "Password Mismatch", "Passwords do not match.")
            return

        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            query = """
                UPDATE Employee 
                SET username = %s, email = %s, password = %s 
                WHERE employee_id = %s
            """
            cursor.execute(query, (username, email, password, self.employee_data['employee_id']))
            conn.commit()

            QtWidgets.QMessageBox.information(self, "Success", "Account updated successfully.")
            print("[DB] Employee settings updated.")

            self.employee_data['username'] = username
            self.employee_data['email'] = email
            self.employee_data['password'] = password

            self.set_account_fields_enabled(False)

        except Exception as e:
            print(f"[ERROR] Update failed: {e}")
            QtWidgets.QMessageBox.critical(self, "Error", f"Update failed:\n{e}")
        finally:
            cursor.close()
            conn.close()

    def populate_leave_types(self):
        # Predefine the leave types and their corresponding IDs
        self.leave_type_mapping = {
            "Sick Leave": 1,  # Assuming '1' is the ID for Sick Leave
            "Casual Leave": 2,  # Assuming '2' is the ID for Casual Leave
            "Paid Leave": 3,  # Assuming '3' is the ID for Paid Leave
        }
        
        # Set the items for the leaveType combo box
        self.ui.leaveRequestType.setItemText(0, "Sick Leave")
        self.ui.leaveRequestType.setItemText(1, "Casual Leave")
        self.ui.leaveRequestType.setItemText(2, "Paid Leave")


    def submit_leave_application(self):
        leave_type_name = self.ui.leaveRequestType.currentText()  # Get selected leave type text
        reason = self.ui.leaveRequestReason.toPlainText().strip()  # Get the reason from the text field
        chosen_qdate = self.ui.leaveRequestCalendar.selectedDate()
        chosen_date = chosen_qdate.toString("yyyy-MM-dd")  # Format the selected date

        if not reason:
            QtWidgets.QMessageBox.warning(self, "Input Error", "Please enter a reason for the leave.")
            return

        if len(reason) > 20:
            QtWidgets.QMessageBox.warning(self, "Input Error", "Reason must not exceed 20 characters.")
            return

        try:
            # Get the leaveType_id from the mapping using the leave type name
            leave_type_id = self.leave_type_mapping.get(leave_type_name)

            if not leave_type_id:
                raise ValueError(f"Unknown leave type: {leave_type_name}")

            # Insert the leave application into the database
            conn = get_db_connection()
            cursor = conn.cursor()
            query = """
                INSERT INTO LeaveApplication (employee_id, date, leaveType_id, reason)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(query, (self.employee_data['employee_id'], chosen_date, leave_type_id, reason))
            conn.commit()

            QtWidgets.QMessageBox.information(self, "Success", "Leave application submitted.")
            self.clear_leave_form()

        except Exception as e:
            print(f"[ERROR] Leave submission failed: {e}")
            QtWidgets.QMessageBox.critical(self, "Error", f"Submission failed:\n{e}")
        finally:
            try:
                cursor.close()
                conn.close()
            except:
                pass


    def clear_leave_form(self):
        self.ui.leaveRequestReason.clear()
        self.ui.leaveRequestCalendar.setSelectedDate(QtCore.QDate.currentDate())
        self.ui.leaveRequestType.setCurrentIndex(0)

    def start_clock(self):
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

    def update_time(self):
        now = datetime.datetime.now()
        formatted = now.strftime("%B %d, %Y %I:%M:%S %p")
        self.ui.dashboardTimeAndDate.setText(
            f"<html><head/><body><p><span style=\" font-size:14pt; font-weight:500;\">{formatted}</span></p></body></html>"
        )

    def show_member_dashboard(self):
        self.ui.memberStackedWidget.setCurrentWidget(self.ui.memberDashboard)

    def show_member_file_leave(self):
        self.ui.memberStackedWidget.setCurrentWidget(self.ui.memberFileLeave)

    def show_member_notification(self):
        self.ui.memberStackedWidget.setCurrentWidget(self.ui.memberNotifications)

    def show_member_settings(self):
        self.update_settings_tab()
        self.ui.memberStackedWidget.setCurrentWidget(self.ui.memberSettings)

    def member_logout_process(self):
        self.welcome_window.show()
        self.close()

    def update_chosen_date(self, date):
        text = date.toString("MMMM d, yyyy")
        self.ui.label_15.setText(
            f'<html><head/><body><p align="center">'
            f'<span style=" font-size:24pt;">Chosen Date: </span>'
            f'<span style=" font-size:24pt; font-weight:600;">{text}</span>'
            f'</p></body></html>'
        )
