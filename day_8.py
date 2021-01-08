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

# 확인
S = {1, 3, 4, 8, 13, 17, 20}
short(S)  # (3, 4) 출력

# 2. 회문(palindrome)? 순서를 거꾸로 해서 읽어도 제대로 읽을 때와 같은 단어 or 문장
# rotator, sos, abba (nurses run)
# 문제 : 임의의 단어(문장)을 입력받아 회문 여부를 출력 =>  True or False 출력
def palindrom(s):
    real_s = s.replace(" ", "")
    if real_s == real_s[::-1]:
        print("True")
    else:
        print("False")

palindrom("rotator")  # True
palindrom("nurses run")  # True
palindrom("palindrom")  # False
