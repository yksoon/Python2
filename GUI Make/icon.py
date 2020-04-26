# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 10:31:22 2020

@author: USER
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class MyApp(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
    def initUI(self):
        
        self.setWindowTitle('Icon') # 창의 제목
        self.setWindowIcon(QIcon('web.png'))
        self.setGeometry(300, 300, 300, 200)
        # setGeometry() 메서드는 창의 위치와 크기를 설정합니다.
        # 앞의 두 매개변수는 창의 x, y 위치를 결정하고, 뒤의 두 매개변수는 각각 창의 너비와
        # 높이를 결정합니다.
        # 이 메서드는 창 띄우기 예제에서 사용했던 move()와 resize() 메서드를 하나로 합쳐놓은
        # 것과 같습니다.
        self.show() # 창 나타내기
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())



