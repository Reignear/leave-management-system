# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'leaderDashboard.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LeaderMainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1554, 877)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.SideBarWidget = QtWidgets.QWidget(self.centralwidget)
        self.SideBarWidget.setGeometry(QtCore.QRect(0, 0, 331, 881))
        self.SideBarWidget.setStyleSheet("QWidget#SideBarWidget{\n"
"background: qlineargradient(x1:0, y1:1, x2:0, y2:0, \n"
"    stop:0 #add8e6, stop:1 #ffffff);\n"
"}")
        self.SideBarWidget.setObjectName("SideBarWidget")
        self.label = QtWidgets.QLabel(self.SideBarWidget)
        self.label.setGeometry(QtCore.QRect(120, 10, 71, 71))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../../OneDrive/Desktop/copy.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.dashboardBTN = QtWidgets.QPushButton(self.SideBarWidget)
        self.dashboardBTN.setGeometry(QtCore.QRect(10, 120, 301, 51))
        self.dashboardBTN.setStyleSheet("font: 10pt \"Arial\";")
        self.dashboardBTN.setObjectName("dashboardBTN")
        self.calendarLeaveBTN = QtWidgets.QPushButton(self.SideBarWidget)
        self.calendarLeaveBTN.setGeometry(QtCore.QRect(10, 390, 301, 51))
        self.calendarLeaveBTN.setStyleSheet("font: 10pt \"Arial\";")
        self.calendarLeaveBTN.setObjectName("calendarLeaveBTN")
        self.teamBTN = QtWidgets.QPushButton(self.SideBarWidget)
        self.teamBTN.setGeometry(QtCore.QRect(10, 210, 301, 51))
        self.teamBTN.setStyleSheet("font: 10pt \"Arial\";")
        self.teamBTN.setObjectName("teamBTN")
        self.leaveRequestBTN = QtWidgets.QPushButton(self.SideBarWidget)
        self.leaveRequestBTN.setGeometry(QtCore.QRect(10, 300, 301, 51))
        self.leaveRequestBTN.setStyleSheet("font: 10pt \"Arial\";")
        self.leaveRequestBTN.setObjectName("leaveRequestBTN")
        self.logoutBTN = QtWidgets.QPushButton(self.SideBarWidget)
        self.logoutBTN.setGeometry(QtCore.QRect(10, 810, 301, 51))
        self.logoutBTN.setStyleSheet("QPushButton#logoutBTN{\n"
" background-color: #FAA0A0;\n"
"font: 10pt \"Arial\";\n"
"}")
        self.logoutBTN.setObjectName("logoutBTN")
        self.dashboardStackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.dashboardStackedWidget.setEnabled(True)
        self.dashboardStackedWidget.setGeometry(QtCore.QRect(340, 0, 1211, 881))
        font = QtGui.QFont()
        font.setKerning(True)
        self.dashboardStackedWidget.setFont(font)
        self.dashboardStackedWidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.dashboardStackedWidget.setToolTip("")
        self.dashboardStackedWidget.setStatusTip("")
        self.dashboardStackedWidget.setWhatsThis("")
        self.dashboardStackedWidget.setStyleSheet("QStackedWidget#dashboardStackedWidget{\n"
" \n"
"}")
        self.dashboardStackedWidget.setObjectName("dashboardStackedWidget")
        self.dashboardPage = QtWidgets.QWidget()
        self.dashboardPage.setObjectName("dashboardPage")
        self.groupBox = QtWidgets.QGroupBox(self.dashboardPage)
        self.groupBox.setGeometry(QtCore.QRect(-10, 0, 1241, 851))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.firstWidget = QtWidgets.QWidget(self.groupBox)
        self.firstWidget.setGeometry(QtCore.QRect(20, 20, 281, 161))
        self.firstWidget.setStyleSheet("QWidget#firstWidget{\n"
"background-color: #E6F4EA;\n"
"border-radius: 10px;\n"
"}")

        self.firstWidget.setObjectName("firstWidget")
        self.totalLeaveLabel = QtWidgets.QLabel(self.firstWidget)
        self.totalLeaveLabel.setGeometry(QtCore.QRect(4, 0, 101, 161))
        self.totalLeaveLabel.setObjectName("totalLeaveLabel")
        self.label_4 = QtWidgets.QLabel(self.firstWidget)
        self.label_4.setGeometry(QtCore.QRect(110, 0, 171, 161))
        self.label_4.setObjectName("label_4")
        self.secondWidget = QtWidgets.QWidget(self.groupBox)
        self.secondWidget.setGeometry(QtCore.QRect(320, 20, 281, 161))
        self.secondWidget.setStyleSheet("QWidget#secondWidget{\n"
"background-color: #E6F0FA;\n"
"border-radius: 10px;\n"
"}")
        self.secondWidget.setObjectName("secondWidget")
        self.label_5 = QtWidgets.QLabel(self.secondWidget)
        self.label_5.setGeometry(QtCore.QRect(110, 0, 171, 161))
        self.label_5.setObjectName("label_5")
        self.totalSickLeaveLabel = QtWidgets.QLabel(self.secondWidget)
        self.totalSickLeaveLabel.setGeometry(QtCore.QRect(0, 0, 111, 161))
        self.totalSickLeaveLabel.setObjectName("totalSickLeaveLabel")
        self.thirdWidget = QtWidgets.QWidget(self.groupBox)
        self.thirdWidget.setGeometry(QtCore.QRect(620, 20, 281, 161))
        self.thirdWidget.setStyleSheet("QWidget#thirdWidget{\n"
"background-color: #EDE9FE;\n"
"border-radius: 10px;\n"
"}")
        self.thirdWidget.setObjectName("thirdWidget")
        self.label_7 = QtWidgets.QLabel(self.thirdWidget)
        self.label_7.setGeometry(QtCore.QRect(110, 0, 171, 161))
        self.label_7.setObjectName("label_7")
        self.TotalCasualLeaveLabel = QtWidgets.QLabel(self.thirdWidget)
        self.TotalCasualLeaveLabel.setGeometry(QtCore.QRect(0, 0, 111, 161))
        self.TotalCasualLeaveLabel.setObjectName("TotalCasualLeaveLabel")
        self.fourthWidget = QtWidgets.QWidget(self.groupBox)
        self.fourthWidget.setGeometry(QtCore.QRect(920, 20, 281, 161))
        self.fourthWidget.setStyleSheet("QWidget#fourthWidget{\n"
"background-color: #FCE7E9;\n"
"border-radius: 10px;\n"
"}")
        self.fourthWidget.setObjectName("fourthWidget")
        self.label_9 = QtWidgets.QLabel(self.fourthWidget)
        self.label_9.setGeometry(QtCore.QRect(110, 0, 171, 161))
        self.label_9.setObjectName("label_9")
        self.totalPaidEarnedLeaveLabel = QtWidgets.QLabel(self.fourthWidget)
        self.totalPaidEarnedLeaveLabel.setGeometry(QtCore.QRect(0, 0, 111, 161))
        self.totalPaidEarnedLeaveLabel.setObjectName("totalPaidEarnedLeaveLabel")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 210, 1181, 631))
        self.groupBox_2.setStyleSheet("QGroupBox {\n"
"    border: none;\n"
"    margin-top: 0px; /* Optional: Adjusts the space above the group box title */\n"
"}\n"
"")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.recentLeaveTable = QtWidgets.QTableWidget(self.groupBox_2)
        self.recentLeaveTable.setGeometry(QtCore.QRect(0, 70, 1181, 451))
        self.recentLeaveTable.setObjectName("recentLeaveTable")
        self.recentLeaveTable.setColumnCount(0)
        self.recentLeaveTable.setRowCount(0)
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setGeometry(QtCore.QRect(4, 5, 211, 61))
        self.label_11.setObjectName("label_11")
        self.leaveRequestTableNextBTN = QtWidgets.QPushButton(self.groupBox_2)
        self.leaveRequestTableNextBTN.setGeometry(QtCore.QRect(1060, 530, 111, 31))
        self.leaveRequestTableNextBTN.setObjectName("leaveRequestTableNextBTN")
        self.leaveRequestTablePrevBTN = QtWidgets.QPushButton(self.groupBox_2)
        self.leaveRequestTablePrevBTN.setGeometry(QtCore.QRect(950, 530, 111, 31))
        self.leaveRequestTablePrevBTN.setObjectName("leaveRequestTablePrevBTN")
        self.dashboardStackedWidget.addWidget(self.dashboardPage)
        self.teamPage = QtWidgets.QWidget()
        self.teamPage.setObjectName("teamPage")
        self.groupBox_3 = QtWidgets.QGroupBox(self.teamPage)
        self.groupBox_3.setGeometry(QtCore.QRect(-10, 0, 1231, 881))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(10, 110, 101, 51))
        self.label_3.setObjectName("label_3")
        self.teamSearchInput = QtWidgets.QLineEdit(self.groupBox_3)
        self.teamSearchInput.setGeometry(QtCore.QRect(100, 110, 401, 51))
        self.teamSearchInput.setStyleSheet("QLineEdit#teamSearchInput{\n"
"    border-radius: 5px;\n"
"font: 10pt \"Arial\";\n"
"}")
        self.teamSearchInput.setObjectName("teamSearchInput")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setGeometry(QtCore.QRect(10, 0, 261, 91))
        self.label_2.setObjectName("label_2")
        self.teamGridGroupBox = QtWidgets.QGroupBox(self.groupBox_3)
        self.teamGridGroupBox.setGeometry(QtCore.QRect(40, 180, 1161, 651))
        self.teamGridGroupBox.setStyleSheet("QGroupBox#teamGridGroupBox {\n"
"    border-radius: 10px;\n"
"    /* Add a background color */\n"
"    border: 1px solid black;  /* Optionally, you can add a border for visibility */\n"
"}\n"
"")
        self.teamGridGroupBox.setTitle("")
        self.teamGridGroupBox.setObjectName("teamGridGroupBox")
        self.teamCard = QtWidgets.QGroupBox(self.teamGridGroupBox)
        self.teamCard.setGeometry(QtCore.QRect(20, 20, 361, 291))
        self.teamCard.setStyleSheet("QGroupBox#teamCard{\n"
"    border-style: solid;\n"
"    border-radius: 10px;\n"
"    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);\n"
"    background-color: white;\n"
"\n"
"}")
        self.teamCard.setTitle("")
        self.teamCard.setObjectName("teamCard")
        self.teamCardBackground = QtWidgets.QWidget(self.teamCard)
        self.teamCardBackground.setGeometry(QtCore.QRect(0, 0, 361, 71))
        self.teamCardBackground.setStyleSheet("QWidget#teamCardBackground {\n"
"background-color: #51158C;\n"
"border-top-left-radius: 10px;\n"
"  border-top-right-radius: 10px;\n"
"\n"
"}")
        self.teamCardBackground.setObjectName("teamCardBackground")
        self.teamCardFirstLetterBackground = QtWidgets.QWidget(self.teamCard)
        self.teamCardFirstLetterBackground.setGeometry(QtCore.QRect(110, 20, 141, 101))
        self.teamCardFirstLetterBackground.setStyleSheet("QWidget#teamCardFirstLetterBackground{\n"
"background-color: white;\n"
"border-radius: 20px;\n"
"}")
        self.teamCardFirstLetterBackground.setObjectName("teamCardFirstLetterBackground")
        self.teamCardFirstLetter = QtWidgets.QWidget(self.teamCardFirstLetterBackground)
        self.teamCardFirstLetter.setGeometry(QtCore.QRect(10, 10, 120, 80))
        self.teamCardFirstLetter.setStyleSheet("QWidget#teamCardFirstLetter{\n"
"background-color: #B163FF;\n"
"border-radius: 10px;\n"
"}")
        self.teamCardFirstLetter.setObjectName("teamCardFirstLetter")
        self.label_6 = QtWidgets.QLabel(self.teamCardFirstLetter)
        self.label_6.setGeometry(QtCore.QRect(10, 5, 101, 61))
        self.label_6.setObjectName("label_6")
        self.TeamCardName = QtWidgets.QLabel(self.teamCard)
        self.TeamCardName.setGeometry(QtCore.QRect(0, 120, 361, 41))
        self.TeamCardName.setObjectName("TeamCardName")
        self.teamCardEmail = QtWidgets.QLabel(self.teamCard)
        self.teamCardEmail.setGeometry(QtCore.QRect(0, 170, 361, 20))
        self.teamCardEmail.setObjectName("teamCardEmail")
        self.teamCardPhone = QtWidgets.QLabel(self.teamCard)
        self.teamCardPhone.setGeometry(QtCore.QRect(0, 200, 361, 20))
        self.teamCardPhone.setObjectName("teamCardPhone")
        self.viewEmployeeBTN = QtWidgets.QPushButton(self.teamCard)
        self.viewEmployeeBTN.setGeometry(QtCore.QRect(70, 237, 211, 41))
        self.viewEmployeeBTN.setObjectName("viewEmployeeBTN")
        self.teamAddBTN = QtWidgets.QPushButton(self.groupBox_3)
        self.teamAddBTN.setGeometry(QtCore.QRect(1022, 110, 181, 51))
        self.teamAddBTN.setStyleSheet("font: 10pt \"Arial\";")
        self.teamAddBTN.setObjectName("teamAddBTN")
        self.dashboardStackedWidget.addWidget(self.teamPage)
        self.attendancePage = QtWidgets.QWidget()
        self.attendancePage.setObjectName("attendancePage")
        self.widget = QtWidgets.QWidget(self.attendancePage)
        self.widget.setGeometry(QtCore.QRect(-10, 0, 1231, 881))
        self.widget.setObjectName("widget")
        self.label_16 = QtWidgets.QLabel(self.widget)
        self.label_16.setGeometry(QtCore.QRect(30, 10, 271, 61))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.widget)
        self.label_17.setGeometry(QtCore.QRect(950, 90, 271, 61))
        self.label_17.setObjectName("label_17")
        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 150, 1191, 711))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.dashboardStackedWidget.addWidget(self.attendancePage)
        self.calendarLeavePage = QtWidgets.QWidget()
        self.calendarLeavePage.setObjectName("calendarLeavePage")
        self.widget_2 = QtWidgets.QWidget(self.calendarLeavePage)
        self.widget_2.setGeometry(QtCore.QRect(0, 0, 1231, 881))
        self.widget_2.setObjectName("widget_2")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.widget_2)
        self.calendarWidget.setGeometry(QtCore.QRect(10, 80, 1191, 781))
        self.calendarWidget.setObjectName("calendarWidget")
        self.label_18 = QtWidgets.QLabel(self.widget_2)
        self.label_18.setGeometry(QtCore.QRect(10, 0, 271, 61))
        self.label_18.setObjectName("label_18")
        self.dashboardStackedWidget.addWidget(self.calendarLeavePage)
        self.leaveRequestPage = QtWidgets.QWidget()
        self.leaveRequestPage.setObjectName("leaveRequestPage")
        self.groupBox_4 = QtWidgets.QGroupBox(self.leaveRequestPage)
        self.groupBox_4.setGeometry(QtCore.QRect(-10, 0, 1221, 871))
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.tableView = QtWidgets.QTableView(self.groupBox_4)
        self.tableView.setGeometry(QtCore.QRect(10, 170, 1201, 691))
        self.tableView.setObjectName("tableView")
        self.leaveRequestComboBox = QtWidgets.QComboBox(self.groupBox_4)
        self.leaveRequestComboBox.setGeometry(QtCore.QRect(930, 110, 271, 51))
        self.leaveRequestComboBox.setStyleSheet("font: 10pt \"Arial\";")
        self.leaveRequestComboBox.setObjectName("leaveRequestComboBox")
        self.leaveRequestSearch = QtWidgets.QLineEdit(self.groupBox_4)
        self.leaveRequestSearch.setGeometry(QtCore.QRect(110, 110, 381, 51))
        self.leaveRequestSearch.setStyleSheet("QLineEdit#leaveRequestSearch{\n"
"border-style: solid;\n"
"border-radius: 5px;\n"
"font: 10pt \"Arial\";\n"
"\n"
"}")
        self.leaveRequestSearch.setObjectName("leaveRequestSearch")
        self.label_8 = QtWidgets.QLabel(self.groupBox_4)
        self.label_8.setGeometry(QtCore.QRect(10, 120, 101, 41))
        self.label_8.setObjectName("label_8")
        self.label_15 = QtWidgets.QLabel(self.groupBox_4)
        self.label_15.setGeometry(QtCore.QRect(20, 10, 271, 61))
        self.label_15.setObjectName("label_15")
        self.dashboardStackedWidget.addWidget(self.leaveRequestPage)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.dashboardStackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.dashboardBTN.setText(_translate("MainWindow", "Dashboard"))
        self.calendarLeaveBTN.setText(_translate("MainWindow", "Calendar of Leave"))
        self.teamBTN.setText(_translate("MainWindow", "Team"))
        self.leaveRequestBTN.setText(_translate("MainWindow", "Leave Request"))
        self.logoutBTN.setText(_translate("MainWindow", "Logout"))
        self.totalLeaveLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">0</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Total Available </span></p><p><span style=\" font-size:11pt; font-weight:600;\">Leaves</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Total Sick</span></p><p><span style=\" font-size:11pt; font-weight:600;\">Leaves</span></p></body></html>"))
        self.totalSickLeaveLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">0</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Total Casual</span></p><p><span style=\" font-size:11pt; font-weight:600;\">Leaves</span></p></body></html>"))
        self.TotalCasualLeaveLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">0</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Total Paid</span></p><p><span style=\" font-size:11pt; font-weight:600;\">Earned Leaves</span></p></body></html>"))
        self.totalPaidEarnedLeaveLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">0</span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Recent Leave Request </span></p></body></html>"))
        self.leaveRequestTableNextBTN.setText(_translate("MainWindow", "Next"))
        self.leaveRequestTablePrevBTN.setText(_translate("MainWindow", "Previous"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Search</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\"> Production Team</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">R</span></p></body></html>"))
        self.TeamCardName.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Reignear Magallanes</span></p></body></html>"))
        self.teamCardEmail.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">reignearm@gmail.com</span></p></body></html>"))
        self.teamCardPhone.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">09075288220</span></p></body></html>"))
        self.viewEmployeeBTN.setText(_translate("MainWindow", "View"))
        self.teamAddBTN.setText(_translate("MainWindow", "Add "))
        self.label_16.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Attendance</span></p></body></html>"))
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">June 3, 2025 09: 46</span></p></body></html>"))
        self.label_18.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Calendar of Leave</span></p></body></html>"))
        self.leaveRequestSearch.setText(_translate("MainWindow", "leave request ni dire"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Search</span></p></body></html>"))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">List of Leave Request </span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_LeaderMainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
