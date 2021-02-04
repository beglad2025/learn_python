# 1. 유클리드 호제법으로 구현
def getGcd(num1, num2):
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1

print(getGcd(14, 35))  #7


# 2. 찬미가 상품을 받을 확률을 구하는 프로그램

import fractions
def getOdds(a, b):
    for i in range(a+1, b+1):
        case = 0
        cnt = 0
        for j in range(1, i+1):
            if i % j == 0:
                cnt += 1
        if cnt % 2 != 0:
            case += 1
    if case != 0:
        res = fractions.Fraction(case, (b-a))
    else:
        res = 0
    return res

print(getOdds(1, 4))  #1/3
print(getOdds(1, 3))  #0


# 3. 두 대의 프린터를 이용하여 전체 문서를 출력하는 데 드는 최소한의 시간

def getPrintTime(p1, p2, page):
    prt_page = 0
    time = 0
    while prt_page < page:
        time += 1
        if time % p1 == 0:
            prt_page += 1
        if time % p2 == 0:
            prt_page += 1
    return time

n = int(input("테스트 케이스의 갯수를 입력하세요: "))
test_cases = []
for i in range(n):
    test_cases.append(list(map(int, input("테스트 케이스를 입력하세요: ").split())))
for tc in test_cases:
    print(getPrintTime(tc[0], tc[1], tc[2]), end=" ")
