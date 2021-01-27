# 1. 숫자를 입력받으면 그에해당하는 자릿수를 출력하는 코드를 작성하라.

def digit(num):
    d = len(list(num))
    print("1" + "0"*(d-1) + "의 자리수")

num = input("입력: ")
digit(num)


# 2. 리스트에 있는 숫자들의 중앙값을 구하는 프로그램을 만들어라.

def median(num_list):
    num_list.sort()  # 중앙값 처리를 위해 오름차순 정렬이 필요
    x = len(num_list)
    if x % 2 == 0:
        m_index = x // 2
        m = (num_list[m_index - 1] + num_list[m_index]) // 2
    else:
        m_index = x // 2
        m = num_list[m_index]
    return m

a = [7, 9, 14]
print(median(a))
b = [24, 31, 35, 49]
print(median(b))
c = [17, 37, 37, 47, 57]
print(median(c))

import statistics  # 통계에서 쓰는 다양한 함수들 있음
test = [100, 200, 50, 90, 300]
print(statistics.median(test))

# 3. 한개의 문자를 삽입, 제거, 변환을 했을때 s1, s2가 동일한지를 판별하는
# OneEditApart 함수를 작성하시오.
# 완전 문제 잘못이해... 다시 풀이

def OneEditApart(s1, s2):
    line = []
    for i in range(len(s1)):
        num = s2.find(s1[i])
        if num != -1:
            line.append(num)
    if len(line) > 1 and line[0] <= line[1]:
        print("true")
    else:
        print("false")

OneEditApart("cat", "dog")
OneEditApart("cat", "cats")
OneEditApart("cat", "cut")
OneEditApart("cat", "cast")
OneEditApart("cat", "at")
OneEditApart("cat", "acts")


# 4. 카카오 신입 공채 1차 코딩 테스트

def secretMap(n, arr1,arr2):
    for i in range(n):
        arr1[i] = list(format(arr1[i], 'b').zfill(n))
        arr2[i] = list(format(arr2[i], 'b').zfill(n))
    l2 = []
    for i in range(n):
        l1 = []
        for j in range(n):
            if arr1[i][j] == '1' or arr2[i][j] == '1':
                l1.append("#")
            else:
                l1.append(" ")
        l2.append("".join(l1))
    return l2

n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
print(secretMap(n, arr1, arr2))

n = 6
arr1 = [46, 33, 33, 22, 31, 50]
arr2 = [27, 56, 19, 14, 14, 10]
print(secretMap(n, arr1, arr2))


temp = bin(9 | 30)[2:].zfill(5)
temp = temp.replace('0', " ")
temp = temp.replace('1', "#")
print(temp)