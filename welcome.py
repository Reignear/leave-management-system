import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

class WelcomePage(QtWidgets.QFrame):
    def __init__(self, stacked_widget):
        super(WelcomePage, self).__init__()
        self.stacked_widget = stacked_widget
        self.leaderLogin = None
        self.memberLogin = None
        loadUi("welcomePage.ui", self)
        self.setWindowTitle("Welcome")
        self.TeamLeaderBTN.clicked.connect(self.openteamleaderloginpage)
        self.TeamMemberBTN.clicked.connect(self.openteammemberloginpage)

    def openteamleaderloginpage(self):
        self.leaderLogin = GotoleaderLogin()
        self.stacked_widget.addWidget(self.leaderLogin)
        self.stacked_widget.setCurrentIndex(self.stacked_widget.currentIndex() + 1)

    def openteammemberloginpage(self):
        self.memberLogin = GotomemberLogin()
        self.stacked_widget.addWidget(self.memberLogin)
        self.stacked_widget.setCurrentIndex(self.stacked_widget.currentIndex() + 1)



class GotoleaderLogin(QMainWindow):
    def __init__(self, stacked_widget):
        super(GotoleaderLogin, self).__init__()
        self.stacked_widget = stacked_widget  # Initialize stacked_widget to None
        loadUi("leaderLoginPage.ui", self)
        self.setWindowTitle("Leader Login")
        self.leaderBackBTN.clicked.connect(self.openWelcomePage)

    def openWelcomePage(self):
        self.stacked_widget.setCurrentIndex(0)
    

class GotomemberLogin(QMainWindow):
    def __init__(self, stacked_widget):
        super(GotomemberLogin, self).__init__()
        self.stacked_widget = stacked_widget  # Initialize stacked_widget to None
        loadUi("memberLoginPage.ui", self)
        self.setWindowTitle("Member Login")
        self.memberBackBTN.clicked.connect(self.openWelcomePage)
    def openWelcomePage(self):
        self.stacked_widget.setCurrentIndex(0)
       



class GotoWelcome(QMainWindow):
    def __init__(self):
        super(GotoWelcome, self).__init__()
        loadUi("welcomePage.ui", self)
        self.setWindowTitle("Welcome")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    widget = QStackedWidget()  # Create QStackedWidget for page navigation
    window = WelcomePage(widget)  # Pass widget to WelcomePage
    widget.addWidget(window)
    widget.setCurrentIndex(0)
    widget.setFixedWidth(1101)
    widget.setFixedHeight(600)
    widget.show()
    sys.exit(app.exec_())