from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys
import pyautogui
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QRect
import requests
from bs4 import BeautifulSoup
import openpyxl

UI_PATH = "07.GUI\네이버지식인크롤링.ui"

class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self,None)
        uic.loadUi(UI_PATH,self)
        # self.test_img.setPixmap(QPixmap(r'C:\alpaco_\07.GUI\dia.png'))
        # self.test_img.setGeometry(QRect(-100, 530, 681, 291))
        self.start_btn.clicked.connect(self.start)
        self.reset_btn.clicked.connect(self.reset)
        self.save_btn.clicked.connect(self.save)
        self.end_btn.clicked.connect(self.end)
        
    def start(self):
        input_keyword = self.keyword.text()
        try :#페이지입력안했을때 꺼지는 오류를 보완하기 위한 try
                input_page = int(self.page.text())        
        except ValueError:
                input_page = 1
        self.result = []
        for i in range(1, input_page + 1):
                self.textBrowser.append(f"{i}번째 페이지 크롤링 중...")
                QApplication.processEvents() # UI업데이트
                response = requests.get(f"https://kin.naver.com/search/list.naver?query={input_keyword}&page={i}")
                html = response.text
                soup = BeautifulSoup(html, 'html.parser')

                # 질문 10개 덩어리 가져오기
                questions = soup.select(".basic1 > li")
                
                for i, question in enumerate(questions, 1):
                        anchor = question.select_one("dt > a")
                        title = anchor.text # 제목
                        link = anchor.attrs['href'] # 링크
                        date = question.select_one(".txt_inline").text # 날짜
                        content = question.select_one("dl > dd:nth-of-type(2)").text # 내용
                        print(i, title, link, date, content, end='\n')
                        self.textBrowser.append(f"{date},{title},{link},{content}\n")
                        self.result.append([title,link,date,content])
                        QApplication.processEvents() # UI업데이트
    def reset(self):
            self.keyword.setText("")
            self.page.setText("")
            self.textBrowser.setText("")
            
    def save(self):
            keyword = self.keyword.text()
            wb = openpyxl.Workbook()
            ws = wb.active # 활성화된 시트 선택
            ws.title = keyword # 시트 이름 변경
            ws.append(['제목','링크','날짜','내용'])
            for res in self.result:
                    ws.append(res)
            wb.save(f'{keyword}.xlsx')
            print("저장되었습니다.")
            
    def end(self):
            sys.exit()
            

QApplication.setStyle("fusion")
app = QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()
sys.exit(app.exec_())
