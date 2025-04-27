#leaderDashboardBackend.py
from PyQt5 import QtWidgets, QtCore
from UI.leaderDashboard import Ui_LeaderMainWindow
from backend.components.team_page import populate_team_tab
from backend.components.leave_request_page import LeaveRequestPage
from backend.components.employee_dialog import show_employee_dialog, show_remove_confirmation
from backend.components.add_employee_dialog_Backend import show_add_employee, save_new_employee
from utils import get_db_connection
from backend.components.dashboard_page import show_dashboard
from backend.components.team_page import show_team
from backend.components.attendance_page import show_attendance
from backend.components.calendar_leave_page import show_calendar_leave
from backend.components.leave_request_page import show_leave_request

class LeaderMainDashboard(QtWidgets.QMainWindow):

    def leader_logout_process(self):
        self.welcome_window.show()
        self.close()

    def __init__(self, welcome_window):
        super().__init__()
        self.ui = Ui_LeaderMainWindow()
        self.ui.setupUi(self)
        self.ui.dashboardStackedWidget.setCurrentWidget(self.ui.dashboardPage)

        self.teamScrollArea = QtWidgets.QScrollArea(self.ui.teamPage)
        self.teamScrollArea.setGeometry(QtCore.QRect(30, 180, 1161, 651))
        self.teamScrollArea.setWidgetResizable(True)
        self.teamScrollArea.setStyleSheet("border: none;")

        # Inside the scroll area, create a container
        self.teamScrollContent = QtWidgets.QWidget()
        self.teamScrollArea.setWidget(self.teamScrollContent)

        # Inside the container, create a groupbox
        self.teamGridGroupBox = QtWidgets.QGroupBox(self.teamScrollContent)
        self.teamGridGroupBox.setStyleSheet("""
        QGroupBox {
            border-radius: 10px;
            background-color: rgba(240, 240, 240, 255);
            border: 2px solid black;
        }
        """)

        # Set layout
        self.teamGridLayout = QtWidgets.QGridLayout(self.teamGridGroupBox)
        self.teamGridGroupBox.setLayout(self.teamGridLayout)

        # Make the grid fill the container
        layout = QtWidgets.QVBoxLayout(self.teamScrollContent)
        layout.addWidget(self.teamGridGroupBox)


        self.welcome_window = welcome_window

        # Connect Navigation Buttons
        self.ui.dashboardBTN.clicked.connect(lambda: show_dashboard(self))
        self.ui.teamBTN.clicked.connect(lambda: show_team(self))
        self.ui.attendanceBTN.clicked.connect(lambda: show_attendance(self))
        self.ui.calendarLeaveBTN.clicked.connect(lambda: show_calendar_leave(self))
        self.ui.leaveRequestBTN.clicked.connect(lambda: show_leave_request(self))

        # View Employee Dialog
        self.ui.viewEmployeeBTN.clicked.connect(lambda: show_employee_dialog(self))

        # Add Employee Dialog
        self.ui.teamAddBTN.clicked.connect(lambda: show_add_employee(self, self.populate_team_tab))

        # Logout
        self.ui.logoutBTN.clicked.connect(self.leader_logout_process)

        # Populate Team at startup
        self.populate_team_tab()

    def populate_team_tab(self):
        from backend.components.team_page import populate_team_tab
        populate_team_tab(self)

    def show_employee_details(self, employee_id):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            query = "SELECT employee_id, firstname, middlename, lastname, suffix, province, city, baranggay, zipcode, username, email FROM Employee WHERE employee_id = %s"
            cursor.execute(query, (employee_id,))
            employee = cursor.fetchone()

            if employee:
                details = f"""
                        Employee ID: {employee[0]}
                        Name: {employee[1]} {employee[2]} {employee[3]}
                        Suffix: {employee[4] or 'N/A'}
                        Province: {employee[5]}
                        City: {employee[6]}
                        Barangay: {employee[7]}
                        Zip Code: {employee[8]}
                        Username: {employee[9]}
                        Email: {employee[10]}
                        """
                QtWidgets.QMessageBox.information(self, "Employee Details", details)
            else:
                QtWidgets.QMessageBox.warning(self, "Not Found", "Employee not found.")

        except Exception as e:
            print(f"[ERROR] Showing employee details: {e}")
            QtWidgets.QMessageBox.critical(self, "Error", f"Failed to load details:\n{e}")

        finally:
            cursor.close()
            conn.close()
