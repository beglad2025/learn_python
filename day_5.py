# 1. a 리스트에서 중복 숫자를 제거해 보자.
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
newa = list(set(a))
print(newa)

# 2. while문을 사용해 1부터 1000까지의 자연수 중 3의 배수이면서 7의 배수인
# 수의 합을 구해 보자.
i = 1
sum = 0
while i <= 1000:
    i += 1
    if i % 3 == 0 and i % 7 == 0:
        sum += i
print(sum)

# 3. while문을 사용하여 다음과 같이 별(*)을 표시하는 프로그램을 작성해 보자.
# 1)
# *
# **
# ***
# ****
# *****
j1 = 0
while j1 < 5:
    j1 += 1
    print("*" * j1)
print("=" * 50)

# 2)
#      *
#     **
#    ***
#   ****
#  *****
j2 = 0
while j2 < 5:
    j2 += 1
    print("{0:>6}".format("*" * j2))
print("=" * 50)

# 3)adv
#      *
#     ***
#    *****
#   *******
#  *********
j3 = 0
while j3 < 9:
    j3 += 1
    if j3 % 2 == 1:
        print("{0:^9}".format("*" * j3))
print("=" * 50)

# 4.
# for문을 사용해 1부터 100까지의 숫자를 출력해 보자.
for k1 in range(1, 101):
    print(k1)
print("=" * 50)

# 4-1.(adv)
# for문을 사용해 2부터 100까지의 숫자 중에서 소수를(prime number) 출력해 보자.
# *소수란? 1과 자기 자신으로만 나누어 떨어지는 수(ex. 2, 3, 5, 7, 11, 13,...)
# 혼자해본 방법..ㅠ 하지만 오류 있음
# for k2 in range(2, 101):
#     for num in (2, k2+1):
#         if k2 % num != 0:
#             print(k2)
# print('=' * 50)
# 어렵게 꼬아서 가지 말자! 원래 계산방식을 구현하려고 하지말고!
# 어떻게 하면 코드가 더 쉽게 쓰여질 수 있을지 고민해보자!

# 5.
# A 학급에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수는 다음과 같다.
# [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
# for문을 사용하여 A 학급의 평균 점수를 구해 보자.
sum = 0
score = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
for l in score:
    sum += l
print(sum/len(score))
print("=" * 50)

# 6. 로또 당첨 번호 제작(adv)
# *주의:중복된 수 나오면 안됨
# 이번 주 로또 당첨 번호 :  3 7 13 22 25 29
import random
lotto = random.sample(range(1, 46), 6)
print('이번 주 로또 당첨 번호 :', lotto)
print("=" * 50)
# set 활용해서 다시 한 번 풀어보기(while도 포함)


# 7. 자판기(pro, 커피 한 잔에 300원이라 가정, 초기 커피는 10개)
# 돈을 넣어 주세요: 500
# 거스름돈 200를 주고 커피를 줍니다.
# 돈을 넣어 주세요: 300
# 커피를 줍니다.
# 돈을 넣어 주세요: 100
# 돈을 다시 돌려주고 커피를 주지 않습니다.
# 남은 커피의 양은 8개입니다.
# 돈을 넣어 주세요: 0
# 종료합니다
money = 1
coffee = 10
while money != 0:
    m = input("돈을 넣어 주세요: ")
    money = int(m)
    if money > 300:
        change = money - 300
        coffee -= 1
        print("거스름돈 {0}를 주고 커피를 줍니다".format(change))
    elif money == 300:
        coffee -= 1
        print("커피를 줍니다.")
    elif money < 300 and money > 0:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("남은 커피의 양은 {0}개입니다.".format(coffee))
    else:
        print("종료합니다")
