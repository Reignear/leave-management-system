from PyQt5 import QtWidgets
from UI.welcomePage import Ui_welcomeFrame

class WelcomePage(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        self.ui = Ui_welcomeFrame()
        self.ui.setupUi(self)


        self.leader_login_window = None
        self.member_login_window = None

        # Connect buttons to navigation methods
        self.ui.TeamLeaderBTN.clicked.connect(self.show_leader_login)
        self.ui.TeamMemberBTN.clicked.connect(self.show_member_login)

    def show_leader_login(self):
        if self.leader_login_window:
            self.hide()
            self.leader_login_window.show()

    def show_member_login(self):
        if self.member_login_window:
            self.hide()
            self.member_login_window.show()

    def go_back_to_welcome(self):
        if self.leader_login_window:
            self.leader_login_window.hide()
        if self.member_login_window:
            self.member_login_window.hide()
        # Show welcome page
        self.show()