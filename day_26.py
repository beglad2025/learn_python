# 1. 임의의 두 수를 입력 받은 후 최소공배수/최대공약수 출력

# 최대공약수
def getGcd(num1, num2):
    while num2 != 0:
        r = num1 % num2
        num1 = num2
        num2 = r
    return num1

# 최소공배수
def getLcm(num1, num2):
    lcm = (num1 * num2) // getGcd(num1, num2)
    return lcm

# 검증
x, y = map(int, input("임의의 두 수를 입력하세요: ").split())  #12 18
print(getGcd(x, y))  #6
print(getLcm(x, y))  #36

# 2. 1~1000에서 각 숫자의 개수 구하기

num = [str(n) for n in range(1, 1000)]
res = {x:0 for x in range(10)}
for i in num:
    for j in i:
        res[int(j)] += 1
print(res)

# 3. 시저암호

def getCaeser(strr, n):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                'U', 'V', 'W', 'X', 'Y', 'Z']
    res = []
    for s in strr:
        if s in alphabet:
            sindex = alphabet.index(s)
            res.append(alphabet[sindex + int(n)])
        else:   # 알파벳 제외한 공백문자나 특수문자의 경우
            res.append(s)
    print("".join(res))

strr = input("암호로 만들려는 문장: ")
n = input("n: ")
getCaeser(strr, n)


# 4.
import random
x = [random.sample(range(1, 50), 5) for i in range(5)]
print(x)

sum = 0
for i in range(5):
    for j in range(5):
        if i-1 in range(5):
            sum += abs(x[i-1][j]-x[i][j])
        if i+1 in range(5):
            sum += abs(x[i+1][j]-x[i][j])
        if j-1 in range(5):
            sum += abs(x[i][j-1]-x[i][j])
        if j+1 in range(5):
            sum += abs(x[i][j+1]-x[i][j])
print(sum)