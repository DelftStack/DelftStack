import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QHBoxLayout,QCheckBox, QApplication)
from PyQt5 import QtCore

class basicWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        layout = QHBoxLayout()
        self.setLayout(layout)
        
        self.checkBoxA = QCheckBox("Select This.")
        self.labelA = QLabel("Not slected.")
        
        self.checkBoxA.stateChanged.connect(self.checkBoxChangedAction)
        
        layout.addWidget(self.checkBoxA)
        layout.addWidget(self.labelA)
        
        self.setGeometry(200, 200, 300, 200)            
                
        self.setWindowTitle('CheckBox Example')
    
    def checkBoxChangedAction(self, state):
        if (QtCore.Qt.Checked == state):
            self.labelA.setText("Selected.")
        else:
            self.labelA.setText("Not Selected.")
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    windowExample = basicWindow()
    windowExample.show()
    sys.exit(app.exec_())
    