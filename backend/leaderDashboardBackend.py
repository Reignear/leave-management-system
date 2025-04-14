import sys

from PyQt5 import QtWidgets
from UI.leaderDashboard import Ui_LeaderMainWindow
from UI.viewEmployeeDialog import Ui_EmployeeDialog
from UI.addEmployeeDialog import Ui_AddEmployeeDialog
from UI.removeConfirmationDialog import Ui_removeConfirmationDialog


class LeaderMainDashboard(QtWidgets.QMainWindow):

    def __init__(self, welcome_window  ):
        super().__init__()
        self.ui = Ui_LeaderMainWindow()
        self.ui.setupUi(self)
        self.ui.dashboardStackedWidget.setCurrentWidget(self.ui.dashboardPage)

        # call welcome window
        self.welcome_window = welcome_window

        #Navigate Stacked Pages
        self.ui.dashboardBTN.clicked.connect(self.show_dashboard)
        self.ui.teamBTN.clicked.connect(self.show_team)
        self.ui.attendanceBTN.clicked.connect(self.show_attendance)
        self.ui.calendarLeaveBTN.clicked.connect(self.show_calendar_leave)
        self.ui.leaveRequestBTN.clicked.connect(self.show_leave_request)

        #Show view employee dialog
        self.ui.viewEmployeeBTN.clicked.connect(self.show_employee_dialog)

        #Show add employee
        self.ui.teamAddBTN.clicked.connect(self.show_add_employee)

        #logout
        self.ui.logoutBTN.clicked.connect(self.leader_logout_process)


    def show_dashboard(self):
        self.ui.dashboardStackedWidget.setCurrentWidget(self.ui.dashboardPage)

    def show_team(self):
        self.ui.dashboardStackedWidget.setCurrentWidget(self.ui.teamPage)

    def show_attendance(self):
        self.ui.dashboardStackedWidget.setCurrentWidget(self.ui.attendancePage)

    def show_calendar_leave(self):
        self.ui.dashboardStackedWidget.setCurrentWidget(self.ui.calendarLeavePage)

    def show_leave_request(self):
        self.ui.dashboardStackedWidget.setCurrentWidget(self.ui.leaveRequestPage)

    def show_employee_dialog(self):
        view_employee_dialog = QtWidgets.QDialog(self)
        ui = Ui_EmployeeDialog()
        ui.setupUi(view_employee_dialog)
        #Show confirmation Dialog
        ui.removeEmployeeBTN.clicked.connect(self.show_remove_confirmation)

        view_employee_dialog.setModal(True)
        view_employee_dialog.exec_()

    def show_remove_confirmation(self):
        view_remove_confirmation = QtWidgets.QDialog(self)
        ui = Ui_removeConfirmationDialog()
        ui.setupUi(view_remove_confirmation)
        ui.confirmationCancelBTN.clicked.connect(view_remove_confirmation.reject)

        view_remove_confirmation.setModal(True)
        view_remove_confirmation.exec_()

    def show_add_employee(self):
        view_add_employee = QtWidgets.QDialog(self)
        ui =Ui_AddEmployeeDialog()
        ui.setupUi(view_add_employee)
        view_add_employee.setModal(True)
        view_add_employee.exec_()

    def leader_logout_process(self):
        self.welcome_window.show()
        self.close()

