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

# x = int(input())
# for i in range(x, 0, -1):
#     print(i)
#
# y = int(input())
# print("\n".join(map(str, range(y, 0, -1))))

# A+B-7
# n = int(input())
# l = []
# for i in range(n):
#     l.append(list(map(int, input().split())))
# for i in range(n):
#     res = l[i][0]+l[i][1]
#     print("Case #{0}: ".format(i+1), res)

# 별 찍기 - 1
# n = int(input())
# for i in range(n):
#     print("*" * (i+1))

# for i in range(int(input())):
#     print('*' * (i+1))

# 별 찍기 - 2
# for i in range(int(input())):
#     print("%5s" % ("*" * (i+1)))

# A+B - 8
# n = int(input())
# l = []
# for i in range(n):
#     l.append(list(map(int, input().split())))
# for i in range(n):
#     res = l[i][0]+l[i][1]
#     print("Case #{0}:".format(i+1), l[i][0],'+',l[i][1],'=',l[i][0]+l[i][1])

# X보다 작은 수
# N, X = input().split()
# res = [str(i) for i in list(map(int, input().split())) if i < int(X)]
# print(" ".join(res))