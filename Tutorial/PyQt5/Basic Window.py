import sys
from PyQt5 import QtWidgets

def basicWindow():
    app = QtWidgets.QApplication(sys.argv)
    windowExample = QtWidgets.QWidget()
    windowExample.setWindowTitle('Basic Window Example')
    windowExample.show()
    sys.exit(app.exec_())

basicWindow()
