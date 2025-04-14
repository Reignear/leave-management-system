from PyQt5 import QtWidgets
from UI.leaderLoginPage import Ui_leaderLoginWindow
from leaderDashboardBackend import LeaderMainDashboard

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
        # Go to dashboard
        self.ui.LeaderLoginBTN.clicked.connect(self.show_leader_dashboard)

    def show_leader_dashboard(self):
        #create dashboard if does not exist
        if not self.leader_dashboard:
            self.leader_dashboard = LeaderMainDashboard()
        #Hide existing page and show dashboard
        self.hide()
        self.leader_dashboard.show()