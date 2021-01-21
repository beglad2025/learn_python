# 1. 3개의 각으로 삼각형의 예각, 직각, 둔각을 구별하는 프로그램을 만들어라.

def decTri(angleList):  # 삼각형 판별하는 함수
    sum = 0
    answer = "삼각형이 아닙니다"
    for i in range(len(angleList)):  # 세 각의 합을 구함
        if angleList[i] != 0:
            sum += angleList[i]
        else:
            sum += 300  # [0,90,90]과 같은 경우가 sum이 180이 될 수 없는 큰 수를 넣어줌
    if sum == 180 and len(angleList) == 3:  # [40,40,50,50]과 같은 경우가 포함되지 못하도록
        for j in range(len(angleList)):
            if angleList[j] > 90:
                angleList[j] = "둔각"
            elif angleList[j] == 90:
                angleList[j] = "직각"
            else:
                angleList[j] = "예각"
    else:
        return answer
    return angleList

def prtTri(angleList):  # 삼각형 판별 결과 출력하는 함수
    res = decTri(angleList)
    if "둔각" in res:
        print("둔각삼각형")
    elif "직각" in res:
        print("직각삼각형")
    elif "예각" in res:
        print("예각삼각형")
    else:
        print(res)

prtTri([60, 60, 60])  # 예각삼각형
prtTri([30, 60, 90])  # 직각삼각형
prtTri([20, 40, 120])  #둔각삼각형
prtTri([0, 90, 90])  # 삼각형이 아닙니다
prtTri([60, 70, 80])  # 삼각형이 아닙니다
prtTri([40, 40, 50, 50])  #삼각형이 아닙니다


# 2. 괄호의 사용이 잘 되었는지 잘못 되었는지 판별 해 주는 프로그램을 작성하시오.

def brk(brckString):
    l = []
    brckList = list(brckString)  # "("보다 ")"가 많을 경우를 생각해야 하므로
    for i in range(len(brckString)):
        if brckString[i] == "(":
            l.append(brckString[i])
            brckList.remove(brckString[i])  # l에 추가된 기호는 삭제
        elif brckString[i] == ")":
            if len(l) > 0:
                l.pop()
                brckList.remove(brckString[i])  # l에 추가된 기호는 삭제
            else:  # "("보다 ")"이 먼저, 많이 나온 경우
                break  # 실행을 멈추므로 l에 추가된 기호를 brckList에서 지우던 것도 중단
    if len(l) == 0 and len(brckList) == 0:  # 정확히 매치가 되었다면 brckList에 어떤 문자도 남지 않았을 것
        print("정상적인 괄호 사용입니다")
    else:
        print("비정상적인 괄호 사용입니다")

brk("((((((())")  # 비정상적인 괄호 사용입니다
brk("()))")  # 비정상적인 괄호 사용입니다
brk("(()()(()")  # 비정상적인 괄호 사용입니다
brk("(()))(")  # 비정상적인 괄호 사용입니다
brk("())(()")  # 비정상적인 괄호 사용입니다
brk("(()((())()))")  # 정상적인 괄호 사용입니다

