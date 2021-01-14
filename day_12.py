# 1. 다나와 -> 노트북 검색 결과
# 1) 노트북 모델명(굵은 글씨)
# 2) 인치
# 3) 등록월
# 4) 평점, 평점을 매긴 건수
from selenium import webdriver
driver = webdriver.Chrome("c:/scrap/chromedriver.exe")
danawaUrl = "http://search.danawa.com/dsearch.php?query=%EB%AC%B4%EC%84%A0%EC%B2%AD%EC%86%8C%EA%B8%B0&tab=main"
driver.get(danawaUrl)
danawa = driver.page_source

from bs4 import BeautifulSoup
soup = BeautifulSoup(danawa, "html.parser")
cleaners = soup.select("#productListArea > div.main_prodlist.main_prodlist_list > ul")

for cleaner in cleaners:
    for i in range(40):
        print("모델명 :", cleaner.select("div.prod_info > p > a")[i].string)
        print("등록월 :", cleaner.select("dl.meta_item.mt_date > dd")[i].string)
        print("평점 :", cleaner.select("dl.meta_item.mt_comment > dd > div.cnt_star > div.point_num > strong")[i].string, "(", cleaner.select("dl.meta_item.mt_comment > dd > div.cnt_opinion > a")[i].string, "건)")


# 2. 1번 문제를 다 해결했다면,
# 1~10페이지까지 노트북에 대한 정보를 추출
from selenium import webdriver
driver = webdriver.Chrome("c:/scrap/chromedriver.exe")
from bs4 import BeautifulSoup

for i in range(1, 10):
    url = "http://search.danawa.com/dsearch.php?query=%EB%AC%B4%EC%84%A0%EC%B2%AD%EC%86%8C%EA%B8%B0&originalQuery=%EB%AC%B4%EC%84%A0%EC%B2%AD%EC%86%8C%EA%B8%B0&previousKeyword=%EB%85%B8%ED%8A%B8%EB%B6%81&volumeType=allvs&page="+"i"+"&limit=40&sort=saveDESC&list=list&boost=true&addDelivery=N&recommendedSort=Y&defaultUICategoryCode=103740&defaultPhysicsCategoryCode=72%7C80%7C81%7C0&defaultVmTab=2389&defaultVaTab=120766&tab=goods"
    driver.get(url)
    cleanerSource = driver.page_source
    soup = BeautifulSoup(cleanerSource, "html.parser")
    cleaners = soup.select("#productListArea > div.main_prodlist.main_prodlist_list > ul")
    for cleaner in cleaners:
        print("{0}페이지 모델명 :".format(i), cleaner.select("div.prod_info > p > a"))
        print("{0}페이지 등록월 :".format(i), cleaner.select("dl.meta_item.mt_date > dd"))
        print("{0}페이지 평점 :".format(i), cleaner.select("dl.meta_item.mt_comment > dd > div.cnt_star > div.point_num > strong"))
        print("{0}페이지 평점 건수 :".format(i), cleaner.select("dl.meta_item.mt_comment > dd > div.cnt_opinion > a"), "건")


# 3. 보배드림 -> 차량정보추출
# 1)연식
# 2)연료
# 3)가격
from selenium import webdriver
driver = webdriver.Chrome("c:/scrap/chromedriver.exe")
bobaeUrl = "https://www.bobaedream.co.kr/mycar/mycar_list.php?gubun=K"
driver.get(bobaeUrl)
bobae = driver.page_source

from bs4 import BeautifulSoup
soup = BeautifulSoup(bobae, "html.parser")
import re

carName = soup.select("div.mode-cell.title > p > a")
carYear = soup.select("div.mode-cell.year > span.text")
carFuel = soup.select("div.mode-cell.fuel > span")
carPrice = soup.select("div.mode-cell.price > b > em")

for i in range(3):
    print("-" * 10)
    print(carName[i].string)
    print("연식 :", re.findall("\d+[/]\d+", str(carYear[i]))[0])
    print("연료 :", carFuel[i].string)
    print("가격 :", carPrice[i].string, "만원")


# 4. 순위와 함께 영화 제목 추출 => popular streaming movies
from selenium import webdriver
driver = webdriver.Chrome("c:/scrap/chromedriver.exe")
moviesUrl = "https://www.rottentomatoes.com/"
driver.get(moviesUrl)
movies = driver.page_source

from bs4 import BeautifulSoup
soup = BeautifulSoup(movies, "html.parser")
moviesName = soup.select("div:nth-child(1) > section > text-list > ul > li")

i = 0
for name in moviesName:
    i += 1
    print("{0}위".format(i), name.select("a:nth-child(1) > span")[0].string)
