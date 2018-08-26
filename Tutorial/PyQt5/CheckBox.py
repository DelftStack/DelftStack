import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QHBoxLayout,QCheckBox, QApplication)

class basicWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        layout = QHBoxLayout()
        self.setLayout(layout)
        
        self.checkBoxA = QCheckBox("Select This.")
        self.labelA = QLabel("Not slected.")
        
        layout.addWidget(self.checkBoxA)
        layout.addWidget(self.labelA)
        
        self.setGeometry(200, 200, 300, 200)            
                
        self.setWindowTitle('CheckBox Example')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    windowExample = basicWindow()
    windowExample.show()
    sys.exit(app.exec_())
    