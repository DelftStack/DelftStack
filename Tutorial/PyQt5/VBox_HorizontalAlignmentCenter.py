import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore


def basicWindow():
    app = QtWidgets.QApplication(sys.argv)
    windowExample = QtWidgets.QWidget()
    buttonA = QtWidgets.QPushButton('Click!')
    labelA = QtWidgets.QLabel('Label Example')
    labelA.setAlignment(QtCore.Qt.AlignCenter)

    v_box = QtWidgets.QVBoxLayout()
    v_box.addWidget(buttonA)
    v_box.addWidget(labelA)

    windowExample.setLayout(v_box)

    windowExample.setWindowTitle('AlignCenter Example')
    windowExample.show()

    sys.exit(app.exec_())

basicWindow()