import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont

from backend.welcomeBackend import WelcomePage
from backend.leaderLoginBackend import LeaderLoginPage
from backend.memberLoginBackend import MemberLoginPage

def main():
    app = QtWidgets.QApplication(sys.argv)

    # Initialize welcome page and login windows
    welcome_window = WelcomePage()
    leader_login_window = LeaderLoginPage(welcome_window)
    member_login_window = MemberLoginPage(welcome_window)

    # Cross-reference login pages with the welcome page
    welcome_window.leader_login_window = leader_login_window
    welcome_window.member_login_window = member_login_window

    # Show the welcome page
    welcome_window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
