from PyQt5 import QtWidgets, QtCore, QtGui
from UI.memberDashboard import Ui_MemberMainWindow
from utils import get_db_connection
import datetime
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


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

        self.setup_dashboard_chart()

    def setup_dashboard_chart(self):
        try:
            layout = QtWidgets.QVBoxLayout(self.ui.dashboardChart)
            layout.setContentsMargins(0, 0, 0, 0)

            # Create ComboBox manually
            self.dashboardChartFilter = QtWidgets.QComboBox()
            self.dashboardChartFilter.addItems(["1 Month", "6 Months", "1 Year"])
            self.dashboardChartFilter.setFixedHeight(30)

            # Create the matplotlib figure
            self.chart_figure = Figure(figsize=(4, 4))
            self.chart_canvas = FigureCanvas(self.chart_figure)

            layout.addWidget(self.dashboardChartFilter)
            layout.addWidget(self.chart_canvas)

            self.dashboardChartFilter.currentIndexChanged.connect(self.update_chart)

            self.update_chart()

        except Exception as e:
            print(f"[ERROR] Setting up dashboard chart: {e}")

    def update_chart(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)

            selected_filter = self.dashboardChartFilter.currentText()
            today = datetime.date.today()

            if selected_filter == "1 Month":
                filter_date = today - datetime.timedelta(days=30)
            elif selected_filter == "6 Months":
                filter_date = today - datetime.timedelta(days=180)
            elif selected_filter == "1 Year":
                filter_date = today - datetime.timedelta(days=365)
            else:
                filter_date = today - datetime.timedelta(days=30)

            query = """
                SELECT lt.name AS leave_type
                FROM LeaveApplication la
                JOIN LeaveType lt ON la.leavetype_id = lt.leavetype_id
                WHERE la.employee_id = %s AND la.status = 'approved' AND la.date >= %s
            """
            cursor.execute(query, (self.employee_data['employee_id'], filter_date))
            results = cursor.fetchall()

            # Count leave types
            sick = sum(1 for r in results if r['leave_type'].lower() == 'sick')
            casual = sum(1 for r in results if r['leave_type'].lower() == 'casual')
            paid = sum(1 for r in results if r['leave_type'].lower() == 'paid')

            self.chart_figure.clear()
            ax = self.chart_figure.add_subplot(111)

            if sick == 0 and casual == 0 and paid == 0:
                ax.text(0.5, 0.5, 'No Data', horizontalalignment='center', verticalalignment='center', transform=ax.transAxes, fontsize=18)
            else:
                labels = ['Sick Leave', 'Casual Leave', 'Paid Leave']
                sizes = [sick, casual, paid]
                colors = ['#ff9999', '#66b3ff', '#99ff99']

                ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors)
                ax.axis('equal')

            self.chart_canvas.draw()

            cursor.close()
            conn.close()

        except Exception as e:
            print(f"[ERROR] Updating chart: {e}")

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
            "Casual Leave": 1,  # Assuming '1' is the ID for Casual Leave
            "Sick Leave": 2,  # Assuming '2' is the ID for Sick Leave
            "Paid Leave": 3,  # Assuming '3' is the ID for Paid Leave
        }
        
        # Set the items for the leaveType combo box
        self.ui.leaveRequestType.setItemText(0, "Casual Leave")
        self.ui.leaveRequestType.setItemText(1, "Sick Leave")
        self.ui.leaveRequestType.setItemText(2, "Paid Leave")


    def submit_leave_application(self):
        leave_type_name = self.ui.leaveRequestType.currentText()  # Get selected leave type text
        reason = self.ui.leaveRequestReason.toPlainText().strip()  # Get the reason from the text field
        chosen_qdate = self.ui.leaveRequestCalendar.selectedDate()
        chosen_date = chosen_qdate.toString("yyyy-MM-dd")  # Format the selected date

        if not reason:
            QtWidgets.QMessageBox.warning(self, "Input Error", "Please enter a reason for the leave.")
            return

        if len(reason) > 100:
            QtWidgets.QMessageBox.warning(self, "Input Error", "Reason must not exceed 100 characters.")
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
        self.populate_notifications_tab()  # Load notifications
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

    def populate_notifications_tab(self):
        try:
            print("[DEBUG] Started populate_notifications_tab()")
            
            self.ui.notificationTable.setColumnCount(3)
            self.ui.notificationTable.setHorizontalHeaderLabels(["Date of Leave", "Reason", "Status"])
            self.ui.notificationTable.horizontalHeader().setStretchLastSection(True)
            self.ui.notificationTable.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
            print("[DEBUG] Table columns and headers set.")


            conn = get_db_connection()
            print("[DEBUG] Database connection established.")

            cursor = conn.cursor(dictionary=True)
            print("[DEBUG] Cursor created successfully.")

            query = """
            SELECT date, reason, status
            FROM LeaveApplication
            WHERE employee_id = %s
            ORDER BY date DESC
            """
            print(f"[DEBUG] About to execute query for employee_id: {self.employee_data['employee_id']}")
            cursor.execute(query, (self.employee_data['employee_id'],))

            results = cursor.fetchall()
            print(f"[DEBUG] Query executed. Number of results: {len(results)}")

            if not results:
                print("[DEBUG] No leave applications found for this employee.")

            # Clear existing rows
            self.ui.notificationTable.setRowCount(0)
            print("[DEBUG] Cleared existing notificationTable rows.")

            for row_num, leave in enumerate(results):
                print(f"[DEBUG] Inserting row {row_num} -> Data: {leave}")

                self.ui.notificationTable.insertRow(row_num)
                print(f"[DEBUG] Inserted empty row at {row_num}")

                # Date column
                formatted_date = leave['date'].strftime("%B %d, %Y") if isinstance(leave['date'], (datetime.date, datetime.datetime)) else str(leave['date'])
                date_item = QtWidgets.QTableWidgetItem(formatted_date)
                date_item.setFlags(QtCore.Qt.ItemIsEnabled)  # Not editable
                self.ui.notificationTable.setItem(row_num, 0, date_item)
                print(f"[DEBUG] Date set: {formatted_date}")

                # Reason column
                reason_text = leave['reason'] if leave['reason'] else "No Reason Provided"
                reason_item = QtWidgets.QTableWidgetItem(reason_text)
                reason_item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.ui.notificationTable.setItem(row_num, 1, reason_item)
                print(f"[DEBUG] Reason set: {reason_text}")

                # Status column
                status_text = leave['status'].capitalize() if leave['status'] else "Unknown"
                status_item = QtWidgets.QTableWidgetItem(status_text)
                status_item.setFlags(QtCore.Qt.ItemIsEnabled)

                # Color coding
                if leave['status'] == 'approved':
                    status_item.setForeground(QtGui.QBrush(QtGui.QColor('green')))
                    status_item.setFont(QtGui.QFont("", weight=QtGui.QFont.Bold))
                    print(f"[DEBUG] Status approved, colored green.")
                elif leave['status'] == 'pending':
                    status_item.setForeground(QtGui.QBrush(QtGui.QColor('orange')))
                    status_item.setFont(QtGui.QFont("", weight=QtGui.QFont.Bold))
                    print(f"[DEBUG] Status pending, colored orange.")
                elif leave['status'] == 'denied':
                    status_item.setForeground(QtGui.QBrush(QtGui.QColor('red')))
                    status_item.setFont(QtGui.QFont("", weight=QtGui.QFont.Bold))
                    print(f"[DEBUG] Status denied, colored red.")
                else:
                    print(f"[DEBUG] Status unknown or invalid: {leave['status']}")

                self.ui.notificationTable.setItem(row_num, 2, status_item)
                print(f"[DEBUG] Status set: {status_text}")

            cursor.close()
            conn.close()
            print("[DEBUG] Database connection closed.")

        except Exception as e:
            print(f"[ERROR] populate_notifications_tab() Exception: {e}")
            QtWidgets.QMessageBox.critical(self, "Error", f"Failed to load notifications: {e}")
