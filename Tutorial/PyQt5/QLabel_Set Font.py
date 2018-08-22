import sys
from PyQt5 import QtWidgets, QtGui

def basicWindow():
    app = QtWidgets.QApplication(sys.argv)
    windowExample = QtWidgets.QWidget()
    labelA = QtWidgets.QLabel(windowExample)
    labelB = QtWidgets.QLabel(windowExample)
    labelA.setText('Times Font')
    labelA.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold))
    labelB.setText('Arial Font')
    labelB.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.Black))
    windowExample.setWindowTitle('Label Example')
    windowExample.setGeometry(100, 100, 300, 200)
    labelA.move(100, 40)
    labelB.move(100, 120)
    windowExample.show()
    sys.exit(app.exec_())

basicWindow()