# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 10:20:06 2020

@author: USER
"""


import sys
from PyQt5.QtWidgets import QApplication, QWidget

class MyApp(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
    def initUI(self):
        
        self.setWindowTitle('My First Application') # 창의 제목
        self.move(300, 300) # 창의 위치
        self.resize(400, 200) # 창의 크기
        self.show() # 창 나타내기
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())


