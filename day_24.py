# 1. 리스트에 있는 숫자들의 최빈값을 구하는 프로그램을 만들어라.

def mostCommen(num_list):
    num_set = list(set(num_list))
    cnt = 0
    most_commen_num = []
    for i in num_set:
        if cnt <= num_list.count(i):
            l = len(most_commen_num)
            if cnt < num_list.count(i) and l > 0:
                for j in range(l):
                    most_commen_num.pop()
            cnt = num_list.count(i)
            most_commen_num.append(i)
    if cnt == 1 or len(most_commen_num) == len(num_set):
        print("없다")
    else:
        print(most_commen_num)


mostCommen([12, 17, 12, 19, 17, 19, 19, 23])  #[19]
mostCommen([26, 37, 26, 37, 91])  #[26, 37]
mostCommen([28, 30, 32, 34, 144])  #없다

from collections import Counter
def mostCommen2(num_list):
    cnt = Counter(num_list)
    cnt_list = cnt.most_common()
    max_num = cnt_list[0][1]
    most_commen_num = []
    for num in cnt_list:
        if num[1] == max_num:
            most_commen_num.append(num[0])
    if len(cnt_list) == len(num_list):
        print("없다")
    else:
        print(most_commen_num)

mostCommen2([12, 17, 12, 19, 17, 19, 19, 23])  #[19]
mostCommen2([26, 37, 26, 37, 91])  #[26, 37]
mostCommen2([28, 30, 32, 34, 144])  #없다

# 2. 복잡한 수라도 약수를 찾아줄 수 있고 개수도 알려주는 프로그램
def factor(num):
    factors = []
    for i in range(1, num+1):
        if num % i == 0:
            factors.append(i)
    print("약수의 개수는", len(factors), end="개 입니다\n")

factor(24)  #약수의 개수는 8개 입니다


# 3. 휴대폰 번호 검사 알고리즘을 작성하시오.

import re
def tel(strr):
    inter = {"영":"0", "일":'1', "이":'2', "삼":'3', "사":'4', "오":'5', "육":'6', "칠":'7', "팔":'8', "구":'9'}
    telNum = "".join([t for t in [i if re.match("[0-9]", i) else inter.get(i) for i in strr] if t != None])
    localNum = ["01"+str(l) for l in range(1, 10)]
    if telNum[:3] == "010" and len(telNum) == 11:
        print(telNum, "true")
    elif telNum[0:3] in localNum:
        if len(telNum) == 10 or len(telNum) == 11:
            print(telNum, "true")
    else:
        print(telNum, "false")

tel("영일영-구구칠8-일구팔사")  #01099781984 true
tel("0일영.칠칠칠팔.이삼사")  #0107778234 false
tel("영 일 칠 삼 칠 오 팔 이 팔 이")  #0173758282 true
tel("영일일 34구구 4 오 9 이")  #01134994592 true

# 4. 카프리카 수
import re

def kaprekar(num):
    if len(num) > 4 or re.match("0000|1111|2222|3333|4444|5555|6666|7777|8888|9999", num):
        return False
    else :
        for i in range(4-len(num)):
            num += "0"
        cnt = 0
        while True:
            numList = list(num)
            numList.sort()
            up = int("".join(numList.copy()))
            numList.reverse()
            down = int("".join(numList.copy()))
            num = str(down - up)
            cnt += 1
            if num == "6174" or cnt > 7:
                break
        if num == "6174":
            return cnt
        elif cnt > 7:
            return False

print(kaprekar("4371"))  #7
print(kaprekar("21"))  #3
print(kaprekar("1"))  #False
print(kaprekar("1111"))  #False
