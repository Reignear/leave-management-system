# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'removeConfirmationDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_removeConfirmationDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(492, 425)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(0, 0, 491, 431))
        self.widget.setStyleSheet("QWidget#widget{\n"
"\n"
"background: qlineargradient(x1:0, y1:1, x2:0, y2:0, \n"
"    stop:0 #add8e6, stop:1 #ffffff);\n"
"}")
        self.widget.setObjectName("widget")
        self.label_15 = QtWidgets.QLabel(self.widget)
        self.label_15.setGeometry(QtCore.QRect(0, 0, 491, 81))
        self.label_15.setObjectName("label_15")
        self.confirmationLineEdit = QtWidgets.QLineEdit(self.widget)
        self.confirmationLineEdit.setGeometry(QtCore.QRect(70, 190, 361, 41))
        self.confirmationLineEdit.setStyleSheet("font: 10pt \"Arial\";")
        self.confirmationLineEdit.setObjectName("confirmationLineEdit")
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setGeometry(QtCore.QRect(70, 140, 191, 41))
        self.label_9.setObjectName("label_9")
        self.confirmationRemoveBTN = QtWidgets.QPushButton(self.widget)
        self.confirmationRemoveBTN.setGeometry(QtCore.QRect(70, 250, 171, 51))
        self.confirmationRemoveBTN.setStyleSheet("QPushButton#confirmationRemoveBTN{\n"
"\n"
" background-color: #FAA0A0;\n"
"font: 10pt \"Arial\";\n"
"}")
        self.confirmationRemoveBTN.setObjectName("confirmationRemoveBTN")
        self.confirmationCancelBTN = QtWidgets.QPushButton(self.widget)
        self.confirmationCancelBTN.setGeometry(QtCore.QRect(260, 250, 171, 51))
        self.confirmationCancelBTN.setStyleSheet("\n"
"\n"
"font: 10pt \"Arial\";")
        self.confirmationCancelBTN.setObjectName("confirmationCancelBTN")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_15.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">CONFIRMATION</span></p></body></html>"))
        self.label_9.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Enter your password:</span></p></body></html>"))
        self.confirmationRemoveBTN.setText(_translate("Dialog", "Remove"))
        self.confirmationCancelBTN.setText(_translate("Dialog", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_removeConfirmationDialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
