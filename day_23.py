# 1. 수량을 입력하면 문자열만 딱빼서 숫자만 반환하는 코드
import re
def returnNum(salary):
    sal = "".join([salary[i] for i in range(len(salary)) if re.match("[0-9]", salary[i])])
    return sal

# 검증
print(returnNum("1w627r00o00p00"))


# 3. 압축할 문자열 s가 매개변수로 주어질 때, 위에 설명한 방법으로 1개 이상
# 단위로 문자열을 잘라 압축하여 표현한 문자열 중 가장 짧은 것의 길이를
# return 하도록 solution 함수를 완성해주세요.

# 주어진 단위로 문자 압축하는 함수
def compress(strr, divisor):
    strList = []
    count = 1
    i = 0
    while i+divisor+divisor <= len(strr):
        if strr[i:i+divisor] == strr[i+divisor:i+divisor+divisor]:
            count += 1
        elif strr[i:i+divisor] != strr[i+divisor:i+divisor+divisor]:
            if count > 1:
                strList.append(str(count))
            strList.append(strr[i:i+divisor])
            count = 1
        i += divisor
    if count > 1:
        strList.append(str(count))
    strList.append(strr[i:])
    newStr = "".join(strList)
    return newStr

# 압축하여 표현한 문자열 중 가장 짧은 것의 길이 출력하는 함수
def shortestCompress(s):
    divisorList = range(1, len(s))
    results = []
    for divisor in divisorList:
        results.append(len(compress(s, divisor)))
    shortest = min(results)
    return shortest

print(shortestCompress("aabbaccc"))  #7
print(shortestCompress("ababcdcdababcdcd"))  #9
print(shortestCompress("abcabcdede"))  #8
print(shortestCompress("abcabcabcabcdededededede"))  #14
print(shortestCompress("xababcdcdababcdcd"))  #17



# 4. 특정 키워드가 몇 개 포함되어 있는지 알려주는 프로그램

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
# result = [3, 2, 4, 1, 0]

import re
def keyWord(words, queries):
    queryList = [x.replace("?", ".") for x in queries]
    result = []
    for q in queryList:
        count = len([w for w in words if re.match(q, w) and len(q) == len(w)])
        result.append(count)
    print(result)
keyWord(words, queries)