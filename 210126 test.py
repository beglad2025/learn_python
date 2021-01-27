# 1. "test.txt"라는 파일에 "big data" 문자열을 저장한 후 다시 그 파일을 읽어서 출력하는 프로그램을 작성하시오.

with open("test.txt", "w") as f:  # 문자열 저장
    f.write("big data")

with open("test.txt", "r") as f:  # 파일 출력
    print(f.readline())

# 2. 다음과 같은 문자열에서 휴대폰 번호 뒷자리인 숫자 4개를 ####로 바꾸는 프로그램을 정규식을 사용하여 작성하시오.
phone = """
park 010-9999-9988
kim 010-9909-7789
lee 010-8789-7768
"""

import re
phone_num = re.compile("(010-\d{4})[-]\d{4}")
print(phone_num.sub("\g<1>-####", phone))


# 3. utf-8로 인코딩하기 위한 meta 태그를 적으시오.

# 답 : <meta charset="UTF-8">

# 4. 네이버 또는 다음에 실린 신문기사를 스크래핑하는 코드를 작성하시오.
# (신문사 및 카테고리는 자유롭게 선택 가능, 1page만)

from selenium import webdriver
driver = webdriver.Chrome("c:/scrap/chromedriver.exe")
news_url = "http://edu.chosun.com/site/data/html_dir/2021/01/25/2021012501782.html"
driver.get(news_url)

import time
time.sleep(2)

from bs4 import BeautifulSoup
news = driver.page_source
soup = BeautifulSoup(news, "html.parser")
content = soup.select("#e_article > div.newsCnt")[0].text

import re
email = re.findall("[a-z]+@[a-z]+[.]com", content)
content = content.replace(email[0], "")  # 기사 끝에 있는 기자 메일주소 제거

print(content)
