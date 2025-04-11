import sys
from PyQt5.QtWidgets import *
from backend.welcome import WelcomePage

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QStackedWidget()
    window = WelcomePage(widget)
    widget.addWidget(window)
    widget.setCurrentIndex(0)
    widget.setFixedWidth(1101)
    widget.setFixedHeight(600)
    widget.show()
    sys.exit(app.exec_())