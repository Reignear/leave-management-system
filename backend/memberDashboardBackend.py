from PyQt5 import QtWidgets
from UI.memberDashboard import Ui_MemberMainWindow

class MemberMainDashboard(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MemberMainWindow()
        self.ui.setupUi(self)

        self.ui.memberStackedWidget.setCurrentWidget(self.ui.memberDashboard)

        self.ui.memberDashboardBTN.clicked.connect(self.show_member_dashboard)
        self.ui.memberFileLeaveBTN.clicked.connect(self.show_member_file_leave)
        self.ui.memberNotificationBTN.clicked.connect(self.show_member_notification)
        self.ui.memberSettingsBTN.clicked.connect(self.show_member_settings)

    def show_member_dashboard(self):
        self.ui.memberStackedWidget.setCurrentWidget(self.ui.memberDashboard)

    def show_member_file_leave(self):
        self.ui.memberStackedWidget.setCurrentWidget(self.ui.memberFileLeave)

    def show_member_notification(self):
        self.ui.memberStackedWidget.setCurrentWidget(self.ui.memberNotifications)

    def show_member_settings(self):
        self.ui.memberStackedWidget.setCurrentWidget(self.ui.memberSettings)
