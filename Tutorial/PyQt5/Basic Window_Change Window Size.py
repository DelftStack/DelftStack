import sys
from PyQt5 import QtWidgets

def basicWindow():
    app = QtWidgets.QApplication(sys.argv)
    windowExample = QtWidgets.QWidget()
    windowExample.setGeometry(100, 100, 400, 400)
    windowExample.setWindowTitle('Window Size Example')
    windowExample.show()
    sys.exit(app.exec_())

basicWindow()
