import sys
from PyQt5 import QtWidgets
from backend.welcomeBackend import WelcomePage
from backend.leaderLoginBackend import LeaderLoginPage
from backend.memberLoginBackend import MemberLoginPage

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    # initialize welcome page
    welcome_window = WelcomePage()

    # Create login pages
    leader_login_window = LeaderLoginPage(welcome_window)
    member_login_window = MemberLoginPage(welcome_window)

    # References the logins
    welcome_window.leader_login_window = leader_login_window
    welcome_window.member_login_window = member_login_window

    # Show the welcome page
    welcome_window.show()

    sys.exit(app.exec_())