# 1. 숫자 및 문자열 분리

def sepStrNum(x):
    numList = [str(a) for a in range(10)]
    l = []
    n = []
    for i in range(len(x)):
        if x[i] in numList:
            n.append(x[i])
        else:
            l.append(x[i])
    print('str :', "".join(l))
    print('int :', "".join(n))

x = input("input:")
sepStrNum(x)



# 2. 가위바위보

가위바위보 게임 설정 함수
import random
def game(y):
    pc = random.choice(["가위", "바위", "보"])
    if y == pc:
        res = "비겼습니다 한번더?"
    elif (y == "가위" and pc == "보") or (y=="바위" and pc=="가위") or (y=="보" and pc=="바위"):
        res = "이겼습니다 가위바위보에 소질이 있으시네요!"
    else:
        res = "안타깝네요 게임에서 패배하셨습니다"
    return res

# 가위바위보 게임 실행
prompt = """
1. 게임을 시작합니다
2. 게임을 종료합니다"""
num = 0
while num != 2:
    print(prompt)
    num = int(input())
    if num == 1:
        y = input("가위, 바위, 보 중 어떤 것을 내시겠습니까? : ")
        print(game(y))
print("게임이 종료되었습니다")


# 3. 로또

import random
def lotto(num):
    win = random.sample(range(1, 46), 6)
    print("현재 당첨번호는", win, "입니다.")
    for i in range(num):
        count = 0
        myNum = random.sample(range(1, 46), 6)
        for j in myNum:
            if j in win:
                count += 1
        if count == 6:
            print("구매하신 추첨번호는", myNum, "이며 1등(10억원)입니다")
        elif count == 5:
            print("구매하신 추첨번호는", myNum, "이며 2등(2백만원)입니다")
        elif count == 4:
            print("구매하신 추첨번호는", myNum, "이며 3등(5만원)입니다")
        elif count == 3:
            print("구매하신 추첨번호는", myNum, "이며 4등(5천원)입니다")
        else:
            print("구매하신 추첨번호는", myNum, "입니다")

z = int(input("로또를 몇 개 구매하시겠습니까? :"))
lotto(z)

