from PyQt5.QtWidgets import QFrame
from PyQt5.uic import loadUi

class GotoLeaderLogin(QFrame):
    def __init__(self):
        super(GotoLeaderLogin, self).__init__()
        loadUi("leaderLoginPage.ui", self)