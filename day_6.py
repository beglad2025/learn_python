# 퀴즈 2
fl = ['test.c', 'test.h', 'sample.py', 'sample2.c']
# 확장자가 c이거나 h인 파일 이름을 모두 화면에 출력

for i in fl:
    res = i.split(".")
    if res[1] == 'c' or res[1] == 'h':
        print(i)


# 1. 리스트에서 20 보다 작은 3의 배수를 출력하라
list_1 = [13, 21, 12, 14, 30, 18]
# 12
# 18
print("=" * 10)
for l1 in list_1:
    if l1 < 20:
        if l1 % 3 == 0:
            print(l1)

# 2. 리스트에서 세 글자 이상의 문자를 화면에 출력하라
list_2 = ["I", "study", "python", "language", "!"]
# study
# python
# language
print("=" * 10)
for l2 in list_2:
    if len(l2) >= 3:
        print(l2)

# 3. 파일 이름이 저장된 리스트에서 확장자를 제거하고 파일 이름만 화면에 출력하라.
list_3 = ['hello.py', 'ex01.py', 'intro.hwp']
# hello
# ex01
# intro
print("=" * 10)
for l3 in list_3:
    name = l3.split(".")
    print(name[0])

# 4. my_list를 아래와 같이 출력하라.
my_list = ["가", "나", "다", "라"]
# 가 나
# 나 다
# 다 라
print("=" * 10)
for i in range(3):
    print(my_list[i], my_list[i+1])

# 5. 반복문과 range 함수를 사용해서 my_list를 아래와 같이 출력하라.
my_list = ["가", "나", "다", "라"]
# 라 다
# 다 나
# 나 가
print("=" * 10)
for i in range(3, 0, -1):
    print(my_list[i], my_list[i-1])

# 6.리스트에 5일간의 저가, 고가 정보가 저장돼 있다. 고가와 저가의 차를 변동폭이라고 정의할 때,
# low, high 두 개의 리스트를 사용해서 5일간의 변동폭을 volatility 리스트에 저장하라.
low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]
print("=" * 10)
volatility = []
for i in range(5):
    value = high_prices[i] - low_prices[i]
    volatility.append(value)
print(volatility)

# 7.리스트에 저장된 데이터를 아래와 같이 출력하라.
apart = [ [101, 102], [201, 202], [301, 302] ]
# 101 호
# 102 호
# -----
# 201 호
# 202 호
# -----
# 301 호
# 302 호
# -----
print("=" * 10)
for i in range(3):
    for j in range(2):
        print(apart[i][j], "호")
    print("-" * 5)


# 8. 구글 입사 test
# 1부터 10,000까지 8이라는 숫자가 총 몇번 나오는가?
# 8이 포함되어 있는 숫자의 갯수를 카운팅 하는 것이 아니라 8이라는 숫자를 모두 카운팅 해야 한다.
# (※ 예를들어 8808은 3, 8888은 4로 카운팅 해야 함)
print("\n")
print("=" * 10)
sum = 0
for i in range(1, 10000):
    str_i = str(i)
    j = str_i.find('8')
    if j != -1:
        sum = sum + str_i.count('8')
print(sum)
