# 1. a 리스트에서 중복 숫자를 제거해 보자.
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
# set 이용한 방법(set은 중복 데이터 허용하지 않으므로)
newa = list(set(a))
print(newa)

# 다른 방법
b = []
for x in a:
    if not x in b:
        b.append(x)
print(b)

# 3. while문을 사용하여 다음과 같이 별(*)을 표시하는 프로그램을 작성해 보자.
# 이중 for문으로 작성해 다시 해보기
# 2)
#      *
#     **
#    ***
#   ****
#  *****
# 방법 1(while 문)
j2 = 0
while j2 < 5:
    j2 += 1
    print("{0:>6}".format("*" * j2))
print("=" * 50)

# 방법 2(for 문)
for i in range(5):
    print("{0:>6}".format("*" * (i + 1)))
print("=" * 50)

# 방법 3(이중 for문으로 하려다 실패..ㅠ)
for i in range(5, 0, -1):
    print(" " * i, end="")
    print("*" * (6 - i))
print("=" * 50)

# 이중 for문으로 하면 만들고자 하는 저 모양이 반복되어 여러번 만들어짐...ㅠ
for i in range(5, 0, -1):
    for j in range(0, i):
        print(" ", end="")
    for k in range(6-i):
        print("*", end="")
    print()
print("=" * 50)



# 3)adv
#      *
#     ***
#    *****
#   *******
#  *********
# 방법 1(while문1)
j3 = 0
while j3 < 9:
    j3 += 1
    if j3 % 2 == 1:
        print("{0:^9}".format("*" * j3))
print("=" * 50)

# 방법 2(while문2)
j3 = -1
while j3 < 9:
    j3 +=2
    print("{0:^9}".format("*" * j3))
print("=" * 50)

# 방법 2(for문)
for i in range(10):
    if i % 2 == 1:
        print("{0:^9}".format("*" * i))
print("=" * 50)

# 4-1.(adv)
# for문을 사용해 2부터 100까지의 숫자 중에서 소수를(prime number) 출력해 보자.
# *소수란? 1과 자기 자신으로만 나누어 떨어지는 수(ex. 2, 3, 5, 7, 11, 13,...)
# 방법 1(혼자)
# l1 = []
# for k1 in range(2, 101):
#     for num in (2, k1+1):
#         if k1 % num != 0:
#             l1.append(k1)
# print(l1)
# print('=' * 50)
# [2, 3, 3, 4, 5, 5, 6, 7, 7, 8, 9, 9, 10, 11, 11, ...] 이런 식으로 출력

# 다른 분 방법1
for k2 in range(2, 101):
    for num in range(2, k2+1):
        if k2 == num:
            print(num, end=' ')
        elif k2 % num == 0:
            break
print("\n")
print('=' * 50)

# 다른 분 방법2
l2 = []
for i in range(2, 101):
    res = True
    for j in range(2, i):
        if i % j == 0:
            res = False
    if res:
        l2.append(i)
print(l2)
print('=' * 50)

# 6. 로또 당첨 번호 제작(adv)
# *주의:중복된 수 나오면 안됨
import random
lotto = random.sample(range(1, 46), 6)
print('이번 주 로또 당첨 번호 :', lotto)
print("=" * 50)

# set 활용해서 다시 한 번 풀어보기
# set & if
lot1 = []
for i in range(20):
    lot1.append(random.randint(1, 45))
    if len(set(lot1)) == 6:
        break
lot1.sort()
print(lot1)

# while
lot2 = []
while True:
    lot2.append(random.randint(1, 45))
    if len(set(lot2)) == 6:
        break
lot2.sort()
print(lot2)
