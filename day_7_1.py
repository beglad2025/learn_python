# 3. 다음과 같은 내용을 지닌 파일 test2.txt가 있다. 이 파일의 내용 중 "java"라는 문자열을
# "python"으로 바꾸어서 저장해 보자.

# 방법1
with open("test2.txt", "w") as t2:
    t2.write("""Life is too short
    you need java""")
with open("test2.txt", "r") as t2:
    s = t2.read()
with open("test2.txt", "w") as t2:
    s = t2.write(s.replace("java", "python"))
with open("test2.txt", "r") as t2:
    s = t2.read()
    print(s)


# 9. 현재 가격을 입력 받아 상한가 (30%)를 출력하는 print_upper_price 함수를 정의하라.



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

# 방법1
not_self_num = set()
for i in range(1, 5000):
    num = i + sum(map(int, str(i)))  # 자기자신 + 각 자리 숫자
    not_self_num.add(num)
self_num = set(range(1, 5000)) - not_self_num
print(self_num)
print(sum(self_num))

# 방법2
list_num = list(range(1, 5000))
set_res = set()
for i in list_num:
    str_num = str(i)
    res = i
    for j in range(len(str_num)):
        res += int(str_num[j])
        set_res.add(res)  # set_res : 셀프 넘버가 아닌 수들
        set_num = set(range(1, 5000))

sol = set_num - set_res
tuple_sol = tuple(sol)
print(set_res)
print(set_num)
print("self number:", sorted(tuple_sol))
print("answer:", sum(tuple_sol))


# 17. 최대 낙차
box = [7, 4, 2, 0, 0, 6, 0, 7, 0]
# 출력 => 최대낙차 : 7
# 방법 1
drop2 = []
for i in range(len(box)):
    drop1 = []
    for j in box[i+1:]:
        if box[i] > j:
            drop1.append(j)
    drop2.append((len(drop1)))
print("최대 낙차 :", max(drop2))


# 방법 2
box = (1, 2, 3, 3, 4, 7, 2, 3)
def maxdrop(arg):
    lres = []
    for j in range(len(arg)):
        num = 0
        for i in arg:
            if arg[j] <= i:
                num += 1
                res = len(arg) - j - num
                lres.append(res)
    print("최대낙차", max(lres))
maxdrop(box)