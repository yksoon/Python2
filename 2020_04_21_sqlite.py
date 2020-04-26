# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 11:28:50 2020

@author: USER
"""

'''
sqlite는 경량 데이터베이스
sqlite3는 파이썬에서 경량 데이터베이스를 사용할수 있게 해주는 모듈
확장자는 .db
자바에서 statement 객체를 생성 시켰듯이 파이썬에서 cursor()함수를 통해 커넥트 시킨다(쿼리문 실행)
'''

import sqlite3

print(sqlite3.version)
print(sqlite3.sqlite_version)

con = sqlite3.connect("C:/Users/USER/Desktop/YKS/Python2/kospi.db")
print(type(con))

cursor = con.cursor()

####

cursor.execute("CREATE TABLE kakao(Date text, Open int, High int, low int, Closing int, Volumn int)")

cursor.execute("INSERT INTO kakao VALUES('16.06.03', 97000, 98600, 96900, 98000, 321405)")

###

cursor.execute("SELECT * FROM kakao")
print(cursor.fetchone())
print(cursor.fetchone())

con.commit()

###

cursor.execute("SELECT * FROM kakao")
print(cursor.fetchall())

###

cursor.execute("SELECT * FROM kakao")
kakao = cursor.fetchall()
print(type(kakao))
print(kakao[0][0])
print(kakao[0][1])
print(kakao[0][2])
print(kakao[0][3])

con.commit()
con.close()





