# web1.py
# 웹크롤링에 관련된 선언
from bs4 import BeautifulSoup

#웹페이지를 로딩
page = open("Chap09_test.html", "rt", encoding="utf-8").read()

#html 파서: "상수값을 지정"
soup = BeautifulSoup(page, "html.parser")

# 원하는 데이터 추출
# print(soup.prettify())

#<p> 태그를 전부 검색
# print(soup.find_all("p"))
#첫번째<p> 태그 검색
# print(soup.find("p"))

#조건검색: <p class="outer-text>
# print(soup.find_all("p", class_="outer-text"))
#attr 속성 검색: attributes
# print(soup.find_all("p", attrs={"class":"outer-text"}))

#태그 내부 문자열 출력: .test속성
for tag in soup.find_all("p"):
    title = tag.text.strip()
    title = title.replace("\n", "")
    print(title)

#id로 검색
print(soup.find(id="first")) 

#첫번쨔 <p> 태그의 속성 검색
# print(soup.find("p")["class"])
#첫번쨔 <p> 태그의 속성 검색
# print(soup.find("p").attrs)
