# 1. IT기업 코딩 테스트문제
# 주어진 문자열(공백 없이 쉼표로 구분되어 있음)을 가지고 아래 문제에 대한
# 프로그램을 작성하세요.
name = ['이유덕','이재영','권종표','이재영','박민호','강상희','이재영','김지완','최승혁','이성연','박영서','박민호','전경헌','송정환','김재성','이유덕','전경헌']
# 김씨와 이씨는 각각 몇 명 인가요?
import re
kim = []
lee = []
for i in name:
    kim += re.findall("김\w{2}", i)
    lee += re.findall("이\w{2}", i)
print("김씨는 {0}명이고, 이씨는 {1}명 입니다".format(len(kim), len(lee)))

# "이재영"이란 이름이 몇 번 반복되나요?
print(name.count("이재영"), "번 반복됩니다")

# 중복을 제거한 이름을 출력하세요.
removeDuplicates = list(set(name))
print(removeDuplicates)

# 중복을 제거한 이름을 오름차순으로 정렬하여 출력하세요.
removeDuplicates.sort()
print(removeDuplicates)


# 2. 토지 원고 데이터
from bs4 import BeautifulSoup
with open("toji.txt", "r", encoding='utf-16') as f:
    tojiFile = BeautifulSoup(f, "html.parser")

# 1) 저자명 추출
print("저자명 :", tojiFile.find("author").string)

# 2) 제목 추출
print("제목 :", tojiFile.title.string)

# 3) 출판사명 추출
print("출판사명 :", tojiFile.find("publisher").string)

# 4) 인용부호(큰 따옴표)로 묶여있는 내용을 모두 추출하여 리스트에 저장
tagP = tojiFile.select("p")
listP = [str(x.string) for x in tagP]
dialogue = []
for i in listP:
    dialogue += re.findall('\"[\w\s,.!?-]+\"', i)

# 5) 토지 원고 전체에서 한글에 해당되는 내용만 추출하여 저장, 가장 많이 사용된 단어 100개를 출력
word = []
for i in listP:
    word += re.findall("[ㄱ-ㅎ가-힣]+", i)

s1 = set(word)
for i in s1:
    word.remove(i)

s2 = set(word)
countKey = []
for j in s2:
    x = word.count(j)
    countKey.append(x)
word_dic = dict(zip(countKey, list(s2)))

dic = sorted(word_dic.items())
values = list(word_dic.values())
print(values)
for k in range(100):
    print("{0}위는".format(k+1), values[-k-1])

# # 6) 각 장의 제목 저장 및 출력
title = tojiFile.find_all("head")
for i in title:
    print(i.string)
