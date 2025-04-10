from PyQt5.QtWidgets import QFrame
from PyQt5.uic import loadUi

class GotoMemberLogin(QFrame):
    def __init__(self):
        super(GotoMemberLogin, self).__init__()
        loadUi("memberLoginPage.ui", self)