from PyQt5 import QtWidgets
from UI.memberLoginPage import Ui_memberLoginWindow
from backend.memberDashboardBackend import MemberMainDashboard

class MemberLoginPage(QtWidgets.QMainWindow):
    def __init__(self, welcome_page):
        super().__init__()
        self.ui = Ui_memberLoginWindow()
        self.ui.setupUi(self)

        # Reference welcome page
        self.welcome_page = welcome_page
        #initialize member dashboard
        self.member_dashboard = None
        # Go back to welcome page
        self.ui.memberBackBTN.clicked.connect(self.welcome_page.go_back_to_welcome)
        # Go to dashboard page
        self.ui.MemberLoginBTN.clicked.connect(self.show_member_dashboard)

    def show_member_dashboard(self):
        self.member_dashboard = MemberMainDashboard(self.welcome_page)
        self.member_dashboard.show()
        self.hide()