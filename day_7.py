# 1. 주어진 자연수가 홀수인지 짝수인지 판별해 주는 함수(is_odd)를 작성해 보자.
def is_odd(a):
    if a % 2 == 0:
        print(a, "은/는 짝수입니다")
    else:
        print(a, "은/는 홀수입니다")

# 확인
is_odd(4)
is_odd(3)

# 2. 다음은 "test1.txt"라는 파일에 "Life is too short" 문자열을 저장한 후
# 다시 그 파일을 읽어서 출력하는 프로그램이다.
# 사용자의 입력을 파일(test.txt)에 저장하는 프로그램을 작성해 보자.
# (단 프로그램을 다시 실행하더라도 기존에 작성한 내용을 유지하고 새로 입력한 내용을 추가해야 한다.)
with open("test1.txt", "a") as t1:
    t1.write("Life is too short\n")
with open("test1.txt", "r") as t1:
    line = t1.readlines()
    for i in line:
        print(i.strip("\n"))

# 3. 다음과 같은 내용을 지닌 파일 test2.txt가 있다. 이 파일의 내용 중 "java"라는 문자열을
# "python"으로 바꾸어서 저장해 보자.
# Life is too short
# you need java
# 주어진 상황 생성
with open("test2.txt", "w") as t2:
    t2.write("Life is too short\n")
    t2.write("you need java\n")
# java -> python
with open("test2.txt", "r") as t2:
    java = t2.readlines()
py = java[1].replace("java", "python")
with open("test2.txt", "w") as t2:
    t2.writelines(java[0] + py)


# 4. "비트코인" 문자열을 화면에 출력하는 print_coin() 함수를 정의하라.
def print_coin():
    print("비트코인")

# 5. 4에서 정의한 함수를 호출하라.
print_coin()

# 6. 4에서 정의한 print_coin 함수를 100번호출하라.
for i in range(100):
    print_coin()

# 7. "비트코인" 문자열을 100번 화면에 출력하는 print_coins() 함수를 정의하라.
def print_coins():
    for i in range(100):
        print("비트코인")

# 확인
print_coins()

# 8. 하나의 문자를 입력받아 문자열 끝에 ":D" 스마일 문자열을 이어 붙여 출력하는
# print_with_smile 함수를 정의하라.
def print_with_smile(a):
    print(a, ":D")

# 확인
print_with_smile("안녕")

# 9. 현재 가격을 입력 받아 상한가 (30%)를 출력하는 print_upper_price 함수를 정의하라.
def print_upper_price(a):
    b = str(int(a * 0.3))
    price = int(a + (a * 0.3 - int(b[-1])))
    str_price = str(price)
    i = int(str_price[-2:])
    if i < 50.0:
        price = price - i
        print(price)
    elif i == 50.0:
        print(price)
    else:
        price = price - (i-50)
        print(price)


# 확인
print_upper_price(9980)


# 10. 하나의 리스트를 입력받아 짝수만 화면에 출력하는 print_even 함수를 정의하라.
def print_even(a):
    for i in a:
        if i % 2 == 0:
            print(i)

# 확인
print_even([1, 2, 3, 4])

# 11. 하나의 딕셔너리를 입력받아 딕셔너리의 key 값을 화면에 출력하는 print_keys 함수를 정의하라.
print_keys = lambda a: print(a.keys())

# 확인
dic = {'아이디':'홍길동', '레벨':10, '체력':100, '마나':20, '공격력':200, '방어력':50}
print_keys(dic)

# 12. 문자열과 한줄에 출력될 글자 수를 입력을 받아 한 줄에 입력된 글자 수만큼 출력하는
# print_mxn(string) 함수를 작성하라.
print_mxn = lambda a, b: print(a[:b])

# 확인
print_mxn("hello world", 7)

# 13. 연봉을 입력받아 월급을 계산하는 calc_monthly_salary(annual_salary) 함수를 정의하라.
# 회사는 연봉을 12개월로 나누어 분할 지급하며, 이 때 1원 미만은 버림한다.
# calc_monthly_salary(12000000)
# 1000000
def calc_monthly(a):
    b = str(a // 12)
    x = int(b[-1])
    if x != 0:
        y = (a // 12) - x
        print(y)

# 확인
calc_monthly(1356333)

# 14. 문자열 하나를 입력받아 인터넷 주소를 반환하는 make_url 함수를 정의하라.
# make_url("naver")
# www.naver.com
make_url = lambda x: print("www.", x, ".com", sep="")

# 확인
make_url("naver")

# 15. 문자열을 입력받아 각 문자들로 구성된 리스트로 반환하는 make_list 함수를 정의하라.
# make_list("abcd")
# ['a', 'b', 'c', 'd']
make_list = lambda x: print(list(x))

# 확인
make_list("abcd")

# 16. 게임 기업 입사문제
# 어떤 자연수 n이 있을 때, d(n)을 n의 각 자릿수 숫자들과 n 자신을 더한 숫자라고 정의하자.
# 예를 들어
# d(91) = 9 + 1 + 91 = 101
# 이 때, n을 d(n)의 제네레이터(generator)라고 한다. 위의 예에서 91은 101의 제네레이터이다.
# 어떤 숫자들은 하나 이상의 제네레이터를 가지고 있는데, 101의 제네레이터는 91 뿐 아니라 100도 있다.
# 그런데 반대로, 제네레이터가 없는 숫자들도 있으며,
# 이런 숫자를 인도의 수학자 Kaprekar가 셀프 넘버(self-number)라 이름 붙였다.
# 예를 들어 1,3,5,7,9,20,31 은 셀프 넘버 들이다.
# 1 이상이고 5000 보다 작은 모든 셀프 넘버들의 합을 구하라.
num = list(range(1, 5000))
for i in range(1, 5000):
    for j in range(1, i):
        newj = list(str(j))
        sum = 0
        for k in range(len(newj)):
            sum = sum + int(newj[k])
        if (sum + j) == i:
            if i in num:
                num.remove(i)
            else:
                continue
all = 0
for x in range(len(num)):
    all = all + num[x]
print(all)


# 17. 최대 낙차
# box = [7, 4, 2, 0, 0, 6, 0, 7, 0]
# 출력 => 최대낙차 : 7
