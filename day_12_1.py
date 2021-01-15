# 1. 다나와 -> 노트북 검색 결과
# 1) 노트북 모델명(굵은 글씨)
# 2) 인치
# 3) 등록월
# 4) 평점, 평점을 매긴 건수
# from selenium import webdriver
# driver = webdriver.Chrome("c:/scrap/chromedriver.exe")  # 드라이버를 로드
# danawaUrl = "http://search.danawa.com/dsearch.php?query=무선청소기&tab=main"
# # url로 접속
# driver.get(danawaUrl)  # 해당url을 브라우저에 띄움

# 참고
# print(driver.current_url)  # 최근 사용한 드라이버url의 주소를 알 수 있음
# driver.implicitly_wait()
# # 웹페이지의 모든 요소(이미지, 텍스트 등)를 모두 읽을 때까지 대기
# # ()안에 3이라고 쓰면 3초 동안 기다려라 이런 의미가 될 수도 있음
# from bs4 import BeautifulSoup
# danawa = driver.page_source
# soup = BeautifulSoup(danawa, "html.parser")
#
# prod_items = soup.select("li.prod_item")
# print(prod_items)
# print("=" * 10)
# print(len(prod_items))

