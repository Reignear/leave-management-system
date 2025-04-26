from PyQt5 import QtWidgets
from UI.leaderLoginPage import Ui_leaderLoginWindow
from backend.leaderDashboardBackend import LeaderMainDashboard


class LeaderLoginPage(QtWidgets.QMainWindow):
    def __init__(self, welcome_page):
        super().__init__()
        self.ui = Ui_leaderLoginWindow()
        self.ui.setupUi(self)

        # Reference welcome page
        self.welcome_page = welcome_page

        # Initialize leader dashboard
        self.leader_dashboard = None

        # Navigate back to welcome page
        self.ui.leaderBackBTN.clicked.connect(self.welcome_page.go_back_to_welcome)
        # Navigate to dashboard
        self.ui.LeaderLoginBTN.clicked.connect(self.show_leader_dashboard)

    def show_leader_dashboard(self):
        self.leader_dashboard = LeaderMainDashboard(self.welcome_page)
        self.leader_dashboard.show()
        self.hide()