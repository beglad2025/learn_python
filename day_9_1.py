# 4. 모스 부호 해독
# 문자열 형식으로 입력받은 모스 부호(dot:. dash:-)를 해독하여
# 영어 문장으로 출력하는 프로그램을 작성하시오.
# 글자와 글자 사이는 공백 1개, 단어와 단어 사이는 공백 2개로 구분한다.
dic = {
    '.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F',
    '--.':'G','....':'H','..':'I','.---':'J','-.-':'K','.-..':'L',
    '--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q','.-.':'R',
    '...':'S','-':'T','..-':'U','...-':'V','.--':'W','-..-':'X',
    '-.--':'Y','--..':'Z'
}

def morse(src):
    res = []
    for word in src.split("  "):  # word에는 단어가 저장, 입력된 문장에 저장된 단어 3개
        for c in word.split(" "):  # c에는 문자가 저장
            res.append(dic[c])
        res.append(" ")  # 단어와 단어가 공백문자로 구분
    return "".join(res)

print(morse('.... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--'))


# 5. ngram 기반 두 문장 유사도 구하기(n=2, 3)
a = "오늘 멀티캠퍼스에서 너무 쉬운 프로그래밍을 공부했다"
b = "멀티캠퍼스에서 공부했던 오늘의 프로그래밍은 너무 쉬웠다"

def ngram(s, num):
    res = []
    slen = len(s)-num+1
    for i in range(slen):
        ss = s[i:i+num]
        res.append(ss)
    return res

def diff_ngram(sa, sb, num):
    a = ngram(sa, num)
    b = ngram(sb, num)
    # print(a)
    # print(b)
    # ['오늘', '늘 ', ' 멀', '멀티', '티캠', '캠퍼', '퍼스', '스에', '에서', '서 ', ' 너', '너무', '무 ', ' 쉬', '쉬운', '운 ', ' 프', '프로', '로그',
    #  '그래', '래밍', '밍을', '을 ', ' 공', '공부', '부했', '했다']
    # ['멀티', '티캠', '캠퍼', '퍼스', '스에', '에서', '서 ', ' 공', '공부', '부했', '했던', '던 ', ' 오', '오늘', '늘의', '의 ', ' 프', '프로', '로그',
    #  '그래', '래밍', '밍은', '은 ', ' 너', '너무', '무 ', ' 쉬', '쉬웠', '웠다']
    cnt = 0 # 일치한 단어의 개수를 저장하기 위한 변수
    r = []  # 일치한 단어를 저장하기 위한 변수
    for i in a:
        for j in b:
            if i == j:  # 두 단어(i, j)가 일치한다면
                cnt += 1
                r.append(i)
    return  cnt/len(a), r


r2, word2 = diff_ngram(a, b, 2)
print("2-gram", r2, word2)  # 유사도, bigram으로 묶인 단어셋

r3, word3 = diff_ngram(a, b, 3)
print("3-gram", r3, word3)  # 유사도, bigram으로 묶인 단어셋

# 수정사항
# 1) 중복허용안되도록
# 2) 두 문장에서 길이가 긴 문장의 단어 개수를 분모

# 내 방법
# str1 = "오늘 멀티캠퍼스에서 너무 쉬운 프로그래밍을 공부했다"
# str2 = "멀티캠퍼스에서 공부했던 오늘의 프로그래밍은 너무 쉬웠다"
# def similarity(str1, str2):
#     str11 = str1.replace(" ", "")
#     str21 = str2.replace(" ", "")
#     s1 = {str11[i:i+2] for i in range(len(str11)-1)}
#     s2 = {str21[i:i+2] for i in range(len(str21)-1)}
#     if len(s1) >= len(s2):
#         print((len(s1 & s2)/len(s1)) * 100, "%의 유사도를 보입니다.")
#     else:
#         print((len(s1 & s2)/len(s2)) * 100, "%의 유사도를 보입니다.")
#
# similarity(str1, str2)