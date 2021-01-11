# 1.다음 입사문제
# 1차원 점들이 주어졌을 때, 그 중 가장 거리가 짧은 것의 쌍을 출력하는 함수를 작성하시오.
# (단, 점들의 배열은 모두 정렬되어 있다고 가정한다.)
# 예를 들어 S = {1, 3, 4, 8, 13, 17, 20}이 주어졌다면, 결과값은 (3, 4)가 될 것이다.
def short(a):
    l = list(a)
    c = []
    sub = l[1]-l[0]
    for i in range(1, len(l)):
        if l[i]-l[i-1] < sub:
            sub = l[i] - l[i-1]
            number = i
    c += [l[number-1], l[number]]
    print(tuple(c))

def find_shortest(number_list):
    result = 0
    min_val = max(number_list)-min(number_list)
    for i in range(len(number_list)-1):
        val = number_list[i+1] - number_list[i]
        if min_val > val:
            min_val = val
            result = i
    return print(number_list[result], number_list[result+1])

# 확인
S = [1, 3, 4, 8, 13, 17, 20]
short(S)  # (3, 4) 출력
find_shortest((S))

# 2. 회문(palindrome)? 순서를 거꾸로 해서 읽어도 제대로 읽을 때와 같은 단어 or 문장
# rotator, sos, abba (nurses run)
# 회문은 유전자 염기서열 분석에도 활용됨(유용한 알고리즘 문제이다!)
# ngram은 검색엔진, 언어패턴 등의 분야에 활용됨.(day9에 배울 내용!)
# 문제 : 임의의 단어(문장)을 입력받아 회문 여부를 출력 =>  True or False 출력
def palindrom1(s):
    real_s = s.replace(" ", "")
    if real_s == real_s[::-1]:
        print("True")
    else:
        print("False")
# 확인
palindrom1("rotator")  # True
palindrom1("nurses run")  # True
palindrom1("palindrom")  # False

# 위에 것을 더 간단하게!
def palindrom2(s):
    real_s = s.replace(" ", "")
    print(real_s == real_s[::-1])

# 확인
palindrom2("rotator")  # True
palindrom2("nurses run")  # True
palindrom2("palindrom")  # False

w1 = input("단어 입력 : ")
isPalindrome = True  # 회문 여부, 초기값
for i in range(len(w1) // 2):
    if w1[i] != w1[-1-i]:
        isPalindrome = False
        break
print(isPalindrome)

# 리스트로 푸는 방법
w2 = input("단어 입력 : ")
print(list(w2) == list(reversed(w2)))

# join 쓰는 법
w3 = input("단어 입력 : ")
print(w3 == ''.join(reversed(w3)))
