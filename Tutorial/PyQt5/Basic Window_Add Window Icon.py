import sys
from PyQt5 import QtWidgets, QtGui

def basicWindow():
    app = QtWidgets.QApplication(sys.argv)
    windowExample = QtWidgets.QWidget()
    windowExample.setWindowTitle('Basic Window Example')
    windowExample.setWindowIcon(QtGui.QIcon("python.jpg"))
    windowExample.show()
    sys.exit(app.exec_())

basicWindow()
