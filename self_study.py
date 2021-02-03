# 알람시계
# 45분 전으로 알람 맞추기

# x, y = input().split()
# if int(y) >= 45:
#     y = int(y) - 45
# elif int(y) < 45:
#     y = int(y) + 15
#     if int(x) != 0:
#         x = int(x) - 1
#     else:
#         x = 23
# print(x, y)

# 고양이

# x = """\    /\\
#  )  ( ')
# (  /  )
#  \(__)|"""
# print(x)

# 개

# y = '''|\\_/|
# |q p|   /}
# ( 0 )"""\\
# |"^"`    |
# ||_/=\\\\__|'''
# print(y)

# 곱셈

# x = input()
# y = input()
# res = 0
# for i in range(len(y)-1, -1, -1):
#     m = int(x) * int(y[i])
#     res += m * (10 ** (len(y)-i-1))
#     print(m)
# print(res)

# import sys
# n = int(sys.stdin.readline().rstrip())
# l = []
# for i in range(n):
#     l.append(list(map(int, sys.stdin.readline().rstrip().split())))
# for j in l:
#     print(j[0]+j[1])

x = int(input())
for i in range(x, 0, -1):
    print(i)

y = int(input())
print("\n".join(map(str, range(y, 0, -1))))