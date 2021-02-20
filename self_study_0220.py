# 1차원 배열

# 1. 최소, 최대
# n = int(input())
# l = list(map(int, input().split()))
# print(min(l), end=" ")
# print(max(l))

# 2. 최댓값
l = []
for i in range(9):
    l.append(int(input()))
print(max(l))
print(l.index(max(l))+1)
