import sys
from PyQt5 import QtWidgets


def basicWindow():
    app = QtWidgets.QApplication(sys.argv)
    windowExample = QtWidgets.QWidget()
    buttonA = QtWidgets.QPushButton('Click!')
    labelA = QtWidgets.QLabel('Label Example')

    h_box = QtWidgets.QHBoxLayout()
    h_box.addStretch()
    h_box.addWidget(labelA)
    h_box.addStretch()

    v_box = QtWidgets.QVBoxLayout()
    v_box.addWidget(buttonA)
    v_box.addLayout(h_box)

    windowExample.setLayout(v_box)

    windowExample.setWindowTitle('QHBoxLayout Example')
    windowExample.show()

    sys.exit(app.exec_())

basicWindow()