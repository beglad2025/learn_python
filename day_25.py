# 1. 초기 투자액과 투자 기간, 그리고 투자 기간 중
# 날짜별 가치 변동율이 주어질 때 순이익과 이익 여부를 구합니다.

def investRes(iv, pr, vc):
    res = iv
    for i in range(pr):
        res = res + (res * vc[i] * 0.01)
    profit = int("{0:.0f}".format(res-iv))
    print(profit)
    if profit > 0:
        print("good")
    elif profit == 0:
        print("same")
    else:
        print("bad")

# investment = int(input("투자액: "))
# period = int(input("투자기간: "))
# value_change = [int(x) for x in input("전일 대비 가치변동: ").split()]
# investRes(investment, period, value_change)

# 투자액: 10000
# 투자기간: 4
# 전일 대비 가치변동: 10 -10 5 -5
# -125
# bad


# 2. 2보다 큰 짝수 n을 입력 받으면, n=p1+p2 를 만족하는
# 소수 p1,p2의 페어를 모두 출력하는 프로그램을 작성하시오.

# 입력받은 수보다 작은 소수 구하는 함수
def getPrime(n):
    primes = [2]
    for i in range(2, n+1):
        a = 0
        for j in primes:
            if i % j == 0:
                a = 1
                break
        if a != 1:
            primes.append(i)
    return primes

# 입력한 수를 만들 수 있는 소수쌍 구하는 함수
def getPrimePair(n):
    primes = getPrime(n)
    prime_pair =[]
    for i in primes:
        if n-i in primes and i <= n-i:
            prime_pair.append([i, n-i])
        if i > n-i:
            break
    return prime_pair

print(getPrimePair(26))  # [[3, 23], [7, 19], [13, 13]]


# 3. 아마존 면접 문제
import re
def getMixArrange(l):
    nlist = []
    slist = []
    for x in l:
        if re.search("[\d]+", x):
            nlist.append(x)
        else:
            slist.append(x)
    nlist.sort()
    slist.sort()
    mix_arrange = [nlist[0]]
    for i in range(1, len(nlist)):
        cnt = 0
        for j in range(len(mix_arrange)):
            if int(mix_arrange[j][1]) <= int(nlist[i][1]):
                cnt += 1
        mix_arrange.insert(cnt, nlist[i])
    mix_arrange += slist
    return mix_arrange

str_list = ['a1', 'a2', 'an', 'b1', 'b2', 'bn']
print(getMixArrange(str_list))
# ['a1', 'b1', 'a2', 'b2', 'an', 'bn']

str_list2 = ['a1', 'a2', 'an', 'c1', 'c3', 'cb', 'b1', 'b2', 'bn']
print(getMixArrange(str_list2))
# ['a1', 'b1', 'c1', 'a2', 'b2', 'c3', 'an', 'bn', 'cb']
