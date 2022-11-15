from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys
UI_PATH = "07.GUI\gmacro.ui"

class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self,None)
        uic.loadUi(UI_PATH,self)
        
        self.StartButton.clicked.connect(self.StartMove)
        
    def StartMove(self):
        input_xpoint = self.xpoint.text()
        input_ypoint = self.ypoint.text()

QApplication.setStyle("fusion")
app = QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()
sys.exit(app.exec_())
