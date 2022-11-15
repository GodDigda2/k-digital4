from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys
import pyautogui
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QRect

UI_PATH = "07.GUI\gmacro.ui"

class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self,None)
        uic.loadUi(UI_PATH,self)
        # self.test_img.setPixmap(QPixmap(r'C:\alpaco_\07.GUI\dia.png'))
        # self.test_img.setGeometry(QRect(-100, 530, 681, 291))
        self.StartButton.clicked.connect(self.StartMove)
        
    def StartMove(self):
        input_xpoint = self.xpoint.text()
        input_ypoint = self.ypoint.text()
        x = int(input_xpoint)
        y = int(input_ypoint)
        pyautogui.moveTo(x, y, 0.3)

QApplication.setStyle("fusion")
app = QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()
sys.exit(app.exec_())
