# 1차원 배열

# 1. 최소, 최대
# n = int(input())
# l = list(map(int, input().split()))
# print(min(l), end=" ")
# print(max(l))

# 2. 최댓값
# l = []
# for i in range(9):
#     l.append(int(input()))
# print(max(l))
# print(l.index(max(l))+1)

# 3. 숫자의 개수
# a = int(input())
# b=  int(input())
# c = int(input())
# x = str(a * b * c)
# for i in range(10):
#     print(x.count(str(i)))

# 4. 나머지
# l = []
# for i in range(10):
#     l.append(int(input()) % 42)
# print(len(set(l)))

# 5. 평균
# n = int(input())
# l = list(map(int, input().split()))
# mx = max(l)
# for i in range(n):
#     l[i] = (l[i] / mx) * 100
# print(sum(l) / n)

# 6. OX퀴즈
n = int(input())
for i in range(n):
    s = input()
    res = 0
    cnt = 0
    for j in range(len(s)):
        if s[j] == "O":
            res += 1
            if j != 0 and s[j-1] == s[j]:
                cnt += 1
                res += cnt
        else:
            cnt = 0
    print(res)