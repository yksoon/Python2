html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.prettify())

# title 태그를 반환
# soup.title
print(soup.title)

# title 태그의 이름('title')을 반환
# soup.title.name
print(soup.title.name)

# title 태그의 문자열을 반환
# soup.title.string
print(soup.title.string)

# title 태그의 부모 태그의 이름을 반환
# soup.title.parent.name
print(soup.title.parent.name)

# 첫 p태그를 반환
# soup.p
print(soup.p)

# 'class' 속성이 있는 첫 p태그를 반환
print(soup.p['class'])

# a 태그를 반환
# soup.a
print(soup.a)

# 모든 a 태그를 리스트 형태로 반환
# soup.find_all()
print(soup.find_all('a'))

# soup.find() : 설정한 값에 해당하는 태그를 반환
# id가 'link3'인 태그를 반환
soup.find(id = 'link3')

# get() : href 속성을 반환
for link in soup.find_all('a'):
    print(link.get('href'))

# get_text() : html 문서 안에 있는 텍스트를 반환
print(soup.get_text())