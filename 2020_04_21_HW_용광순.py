# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 16:46:47 2020

@author: USER
"""


import errno
from bs4 import BeautifulSoup

import requests, re, os
from urllib.request import urlretrieve # 추가

# 저장 폴더를 생성
try:
    if not (os.path.isdir('디지털_가전')):
        os.makedirs(os.path.join('디지털_가전'))
        print("image 폴더 생성 성공!")
except OSError as e:
    if e.errno != errno.EEXIST:
        print("폴더 생성 실패!")
        exit()
        
# 웹페이지를 열고 소스 코드를 읽어오는 작업
html = requests.get("https://search.shopping.naver.com/best100v2/detail.nhn?catId=50000003")
soup = BeautifulSoup(html.text, 'html.parser')
html.close()

# 제품 영역 추출하기
data1_list = soup.findAll('div',{'class':'sr_goods_gallery2 sr_goods_gallery3'})
print(data1_list)

# 전체 제품 리스트
li_list = []

for data1 in data1_list:
    # 제목+썸네일 영역 추출
    # 해당 부분을 찾아 li_list와 병합
    li_list.extend(data1.findAll('li'))

print(li_list)

# 각각 썸네일과 제목 추출하기
for li in li_list:
    img = li.find('img')
    title = img['alt']
    img_src = img['data-original']
    
    # 해당 영역의 글자가 아닌것은 ''로 치환시킨다.
    title = re.sub('[^0-9a-zA-Zㄱ-힗]', '', title)
    
    # 주소, 파일경로 + 파일명 + 확장자
    urlretrieve(img_src, './디지털_가전/' + title + '.jpg')
    

# DB작업을 위한 모듈 import
import pandas as pd
import sqlite3

# DB 테이블 생성
con = sqlite3.connect("C:/Users/USER/Desktop/YKS/Python2/디지털_가전.db")
cursor = con.cursor()
cursor.execute("CREATE TABLE shopping(Name text, Price int)")
con.commit()

# 이름 추출
name_list = []

for li in li_list:
    name = li.find('a')
    title = name['title']
    
    # append
    name_list.append(title)

print(name_list)

# 가격 추출
price_list = []

for li in li_list:
    span = li.find('span',{'class':'num'}).text
    span = re.sub('[^0-9a-zA-Zㄱ-힗]', '', span)
    span = int(span)
    # append
    price_list.append(span)

print(price_list)


# 데이터프레임 생성
from pandas import Series, DataFrame

raw_data = {'제품명' : name_list,
            '가격' : price_list}

data = DataFrame(raw_data)

print(data)

data.to_sql('digital', con, chunksize=1000, index = False)

readed_df = pd.read_sql("SELECT * FROM digital", con)
print(readed_df)

# cursor.execute("DROP TABLE digital")
