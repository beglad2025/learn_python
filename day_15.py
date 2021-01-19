# 1. 두 개의 버전을 비교하는 프로그램을 작성하시오.
def compVer(x, y):
    listX = x.split(".")
    listY = y.split(".")
    i = 0
    while i < 3:  # listX와 listY는 요소가 총 3개 이므로
        if int(listX[i]) > int(listY[i]):
            print(x, ">", y)
            break
        elif int(listX[i]) < int(listY[i]):
            print(x, "<", y)
            break
        else:
            i += 1
            continue  # 위로 돌아가 다시 시행해보시오

x, y = input("비교하고자 하는 버전을 적어주세요 : ").split(" ")
compVer(x, y)


# 2. 총 인원수(N)와 간격(K)이 주어졌을 때 가장 마지막에 살아남는 병사의 위치를 알아내는 것
def safePosition(N, K):
    n = int(N)
    k = int(K)
    member = [x for x in range(1, n+1)]  # 사람의 자리마다 번호를 붙인 리스트 생성
    count = 0
    while True:
        removeList = []  # 이 리스트에 제거대상을 넣을 것이다.
        for i in member:
            count += 1  # 사람 한 명 마다 1씩 카운트를 하고
            if count == k:  # 지정해준 번호의 사람이 되면 제거대상 리스트에 올리고 카운트를 0으로 되돌려라
                removeList.append(i)
                count = 0
        for j in removeList:  # 제거대상인 사람들을 member 리스트에서 제거
            member.remove(j)
        if len(member) == 1:   # 사람이 1명 남으면 while문을 빠져나가라
            break
    return member[0]

N, K = input("총 인원수와 간격을 순서대로 작성해주세요 : ").split(" ")
print(safePosition(N, K))

# 3. 텍스트가 입력으로 주어질 때, 단어의 개수를 세는 프로그램 작성
with open("wikipedia.txt", "r") as f:
    wikipedia = f.readlines()

# ',', '.', '\n' 등 제거
wikipedia = [wikipedia[0].replace(",", "").replace(".", "").replace("\n", "")]
wordList = wikipedia[0].split(" ")  # 공백문자 기준으로 문자열 나눔
wordSet = list(set(wordList))  # 중복 단어 제거한 리스트 생성

num = []
for i in wordSet:
    num.append(wordList.count(i))  # 단어의 반복 횟수 카운트 해 num 리스트에 넣음

# [(반복횟수, '단어'), ...] 형태의 리스트를 반복횟수 높은 것에서 낮은 것 순서로 배열
wordRank = list(reversed(sorted(list(zip(num, wordSet)))))

for i in range(10):  # 10위까지의 단어 출력
    print(wordRank[i][1], wordRank[i][0])



