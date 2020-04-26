# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 16:10:28 2020

@author: USER
"""

# 썸네일 추출 및 다운로드

# 다운로드 하기

'''
이미지 또는 동영상 링크가 있다면 다운로드 하는 방법은 쉽다.
from urllib.request import urlretrieve 를 추가한 뒤,
urlretrieve 호출 시에 링크와 저장 할 파일명을 넣으면 된다.
'''

# 특수문자 처리
'''
도중에 에러가 난 부분을 보면 파일명에 특수문자가 있는 경우,
따라서 추출한 제목에서 특수문자는 다른 문자로 변경해주거나 삭제.

변경은 replace를 하면 되는데,
여기서는 정규식 표현을 이용한 re모듈을 사용하여 삭제.
따라서 re모듈을 import
'''

# 저장폴더 생성
'''
여기서는 os 모듈을 참조
os.path.isdir : 이미 디렉토리가 있는지 검사
os.path.join : 현재 경로를 계산하여 입력을 ㅗ들어온 텍스트를 합하여 새로운 경로를 만듦

os.makedirs : 입력으로 들어온 경로로 폴더를 생성

모듈 참조와 아래 urlretrieve 부분도 변경
'''
import errno
from bs4 import BeautifulSoup

import requests, re, os
from urllib.request import urlretrieve # 추가