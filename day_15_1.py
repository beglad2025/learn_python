# 2. 요세푸스 문제

def sol(n, k):
    a = list(range(1, n+1))
    j = k - 1  # j = 3-1 = 2
    b = 0
    # a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    while (len(a)>1):
        b = (len(a)+b) % k  # (10+0)%3 => 나머지 = 1, b = 1
        del a[j::k]  # a=(1,2, ,4,5, ,7,8, ,10)
        j = k - b - 1  # j = 3 - 1 - 1 = 1 => j = 1

    return a

print(sol(10, 3))


# 3. 가장 많이 쓰인 문자
from collections import Counter
with open("wikipedia.txt", "r") as f:
    words = [w.strip(".,\n") for w in f.read().split()]

# Counter(words).most_common(10)  # 가장 많이쓰인 10개만 출력하라

for w, c in Counter(words).most_common(10):
    print(w, c)