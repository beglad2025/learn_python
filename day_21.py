# 1. 다트 게임

def dartScore(dartResult):
    dartL = list(dartResult)
    for i in range(len(dartResult)):
        # "*"가 있는 해당점수와 그 앞 점수에 "*2"를 넣어주는 과정
        if dartResult[i] == "*":
            dartL[i] = "*2"
            # "*"가 있는 점수가 일의 자리인 경우
            if i-3 > 0 and dartResult[i-3] in ['S', 'D', 'T']:
                dartL[i-3] = dartL[i-3] + "*2"
            # "*"가 있는 점수가 10점인 경우
            elif i-4 > 0 and dartResult[i-4] in ['S', 'D', 'T']:
                dartL[i-4] = dartL[i-4] + "*2"
        # "#"을 "*(-1)"로 넣어주는 과정
        elif dartResult[i] == "#":
            dartL[i] = "*(-1)"
    # "+" 추가하는 과정
    for i in range(len(dartL)-1):
        # 스타상도 아차상도 없는 점수의 경우
        if (dartL[i] in ['S', 'D', 'T']) and ("*" not in dartL[i+1]):
            dartL[i] = dartL[i] + '+'
        # 스타상이나 아차상의 효과가 중첩될 때
        elif ("*" in dartL[i]) and ("*" in dartL[i+1]):
            dartL[i+1] = dartL[i+1] + '+'
        # 스타상이나 아차상의 효과가 한번만 있을 때
        elif ("*" in dartL[i]):
            dartL[i] = dartL[i] + '+'
    newDartResult = ("".join(dartL))
    score = eval(newDartResult.replace("S", "**1").replace("D", "**2").replace("T", "**3"))
    return score


print(dartScore("1S2D*3T"))  # 37
print(dartScore("1D2S#10S"))  # 9
print(dartScore("1D2S0T"))  # 3
print(dartScore("1S*2T*3S"))  # 23
print(dartScore("1D#2S*3S"))  # 4
print(dartScore("1T2D3D#"))  # -4
print(dartScore("1D2S3T*"))  # 59



# 2. DB 캐시를 적용할 때 캐시 크기에 따른 실행시간 측정 프로그램을 작성하시오.
# LUR는 가장 오래전에 참조된 데이터를 교체하는 알고리즘

def runTime(cacheSize, cities):
    citiesName = [c.lower() for c in cities]
    cache = []
    time = 0
    for i in range(len(citiesName)):
        if citiesName[i] not in cache:  # cache 내에 없는 경우
            cache.append(citiesName[i])
            time += 5
            if len(cache) > cacheSize:  # cache 용량 초과한 경우
                del cache[0]  # 맨앞에 있는(가장 오래된) data 삭제
        elif citiesName[i] in cache:  # cache 내에 있는 경우
            cache.remove(citiesName[i])  # 가장 오래된 data가 갱신되어야 하므로
            cache.append(citiesName[i])  # 제거하고 다시 넣어줌
            time += 1
    return time

cacheSize1 = 3
cities1 = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
print(runTime(cacheSize1, cities1))  # 50

cacheSize2 = 3
cities2 = ["Jeju", "Pangyo", 'Seoul', "Jeju", "Pangyo", 'Seoul', 'Jeju', 'Pangyo', 'Seoul']
print(runTime(cacheSize2, cities2))  # 21

cacheSize3 = 2
cities3 = ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'SanFrancisco', 'Seoul', 'Rome', 'Paris', 'Jeju', 'NewYork', 'Rome']
print(runTime(cacheSize3, cities3))  # 60

cacheSize4 = 5
cities4 = ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'SanFrancisco', 'Seoul', 'Rome', 'Paris', 'Jeju', 'NewYork', 'Rome']
print(runTime(cacheSize4, cities4))  # 52

cacheSize5 = 2
cities5 = ['Jeju', 'Pangyo', 'NewYork', 'newyork']
print(runTime(cacheSize5, cities5))  # 16

cacheSize6 = 0
cities6 = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
print(runTime(cacheSize6, cities6))  # 25




# 3. 입력 체크(JS)
# 입력박스, 버튼
# 입력박스에 데이터(아이디) 입력 -> 버튼 클릭 -> 검증(아이디가 6자 이상 12자 이하면 사용가능
# 그렇지 않으면 -> 사용불가)
# <input type="text" id = "myid"/>
# <input type="button" id="chk" value="validation" onclick="
# 작성해야하는 부분
# document.getElementByld('myid').value;
# "/>