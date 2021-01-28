# 1. 직각삼각형의 밑변이 x, 높이가 y일 때
# 남은 변(대각선)의 길이를 구하는 함수를 만들어주세요.

def rightTri(x, y):
    diagonal = (x ** 2 + y ** 2) ** 0.5
    return diagonal

#검증
print(rightTri(3, 4))   # 5.0

# 뉴스 클러스터링

import re
# jacquard2 함수 이전에 전처리 하는 함수
def preJacquard2(str1):
    str1 = str1.lower()
    strList1 = []
    reS = re.compile("[^a-z가-힣]+")
    for i in range(len(str1)-1):
        if reS.search(str1[i:i+2]):
            continue
        else:
            strList1.append(str1[i:i+2])
    return strList1

# n=2일 때 자카드 유사도 구하는 함수
def jacquard2(strList1, strList2):
    strSet1 = set(strList1)
    strSet2 = set(strList2)
    x = 0  # 교집합 개수
    y = 0  # 합집합 개수
    # 두 문자열 중 하나라도 공집합이라 나눗셈이 정의되지 않는 경우
    if len(strSet1) == 0 or len(strSet2) == 0:
        ans = 1 * 65536
    # 비교하고자 하는 문자열 모두 공집합이 아닌 경우
    else:
        while len(strSet1) > 0 and len(strSet2) > 0:  # 둘 중 하나라도 0이면 끝난다
            # 비교하고자 하는 문자열 둘 중 하나라도 리스트 내에 중복없는 경우
            if len(strList1) == len(strSet1) or len(strList2) == len(strSet2):
                x += len(strSet1 & strSet2)
                y += (len(strList1) + len(strList2) - len(strSet1 & strSet2))
                break
            # 비교하고자 하는 문자열 모두 리스트 내에 중복 있는 경우
            else:
                inter = list(strSet1 & strSet2)  # 교집합
                out = list(strSet1 | strSet2)  # 합집합
                x += len(inter)
                y += len(out)
                # 교집합에 포함된 요소 삭제
                for i in range(len(inter)):
                    strList1.remove(inter[i])
                # 교집합에 포함된 요소 삭제된 리스트에서 집합(set) 다시 정의
                strSet1 = set(strList1)
                for j in range(len(out)):  # 두번째 문자열도 위와 똑같이 처리
                    strList2.remove(out[j])
                strSet2 = set(strList2)
                continue
        ans = int((x / y) * 65536)
    return ans

# 클러스터링 결과 얻는 함수
def clustring(str1, str2):
    strList1 = preJacquard2(str1)
    strList2 = preJacquard2(str2)
    res = jacquard2(strList1, strList2)
    print(res)


# 검증
str1, str2 = "FRANCE", "french"
clustring(str1, str2) # 16384

str1, str2 = "handshake", "shake hands"
clustring(str1, str2)  # 65536

str1, str2 = "aa1+aa2", "AAAA12"
clustring(str1, str2)  # 43690

str1, str2 = "E=M*C^2", "e=m*c^2"
clustring(str1, str2)  # 65536

