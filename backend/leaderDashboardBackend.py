from PyQt5 import QtWidgets
from UI.leaderDashboard import Ui_LeaderMainWindow

class LeaderMainDashboard(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LeaderMainWindow()
        self.ui.setupUi(self)

        self.ui.dashboardStackedWidget.setCurrentWidget(self.ui.dashboardPage)

        self.ui.dashboardBTN.clicked.connect(self.show_dashboard)
        self.ui.teamBTN.clicked.connect(self.show_team)
        self.ui.attendanceBTN.clicked.connect(self.show_attendance)
        self.ui.calendarLeaveBTN.clicked.connect(self.show_calendar_leave)
        self.ui.leaveRequestBTN.clicked.connect(self.show_leave_request)

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
