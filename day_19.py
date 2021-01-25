# 1. 구글 전화면접 문제
# 음의 정수는 앞쪽에 양의 정수는 뒷쪽에 있어야 한다.
# 또한, 양의 정수와 음의 정수의 순서는 변함이 있어야한다.

def lineUp(x):
    negative=[]
    pasitive=[]
    for i in x:
        if int(i) > 0:
            pasitive.append(i)
        else:
            negative.append(i)
    print(" ".join(negative), end=" ")
    print(" ".join(pasitive))

x = input("배열을 입력해주세요: ").split(" ")
lineUp(x)


# 2. 총 페이지수를 리턴하는 프로그램

def numOfPage(m, n):
    page = divmod(m, n)
    if page[1] > 0:
        print("총페이지수 :", page[0]+1)
    else:
        print("총페이지수 :", page[0])

m, n = map(int, input("총건수와 한페이지 당 게시물 수를 입력해주세요 :").split(" "))
numOfPage(m, n)


# 3. 회전된 리스트를 문자열로 출력

def trunList(s):
    l = s[1:]
    standard = int(s[0])
    if standard > 0:
        for i in range(standard):
            a = l.pop()
            l = [a] + l
    else:
        for j in range(abs(standard)):
            b = l[0]
            del l[0]
            l += [b]
    print("출력결과:", " ".join(l))

s = input("회전하는 양과 각 항목의 값을 순서대로 작성해주세요: ").split(" ")
trunList(s)


