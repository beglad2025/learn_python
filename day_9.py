# 1. 문자열 바꾸기
# 다음과 같은 문자열이 있다.
# a:b:c:d
# 문자열의 split와 join 함수를 사용하여 위 문자열을 다음과 같이 고치시오.
# a#b#c#d
x = "#".join("a:b:c:d".split(":"))
print(x)

# 2. 리스트 총합 구하기
# 다음은 A학급 학생의 점수를 나타내는 리스트이다.
# 다음 리스트에서 60점 이상 점수의 평균을 구하시오.
A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
high_scores = [x for x in A if x >= 60]
print(sum(high_scores)/len(high_scores))

# 3. 평균값 구하기
# 다음과 같이 총 10줄로 이루어진 sample.txt 파일이 있다.
# sample.txt 파일의 숫자 값을 모두 읽어 총합과 평균 값을 구한 후
# 평균 값을 result.txt 파일에 쓰는 프로그램을 작성하시오.
# 70
# 60
# 55
# 75
# 95
# 90
# 80
# 80
# 85
# 100

# 문제에 주어진 형식의 sample.txt 파일 만들기
with open("sample.txt", "w") as f:
    f.write("""70
60
55
75
95
90
80
80
85
100""")

# 문제 풀이
with open("sample.txt", "r") as f1:
    l = f1.readlines()
    list = []
    for i in l:
        list.append(i.strip("\n"))
    for j in range(len(list)):
        list[j] = int(list[j])
total = sum(list)
average = total/len(list)

with open("result.txt", "w") as f2:
    f2.write("평균값은 {0}입니다.".format(average))

# 4. 모스 부호 해독
# 문자열 형식으로 입력받은 모스 부호(dot:. dash:-)를 해독하여
# 영어 문장으로 출력하는 프로그램을 작성하시오.
# 글자와 글자 사이는 공백 1개, 단어와 단어 사이는 공백 2개로 구분한다.
# 예를 들어 다음 모스 부호는 "HE SLEEPS EARLY"로 해석해야 한다.
# .... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--
# 모스부호 규칙 표
# 문자	부호	문자	부호
# A	.-	N	-.
# B	-...	O	---
# C	-.-.	P	.--.
# D	-..	Q	--.-
# E	.	R	.-.
# F	..-.	S	...
# G	--.	T	-
# H	....	U	..-
# I	..	V	...-
# J	.---	W	.--
# K	-.-	X	-..-
# L	.-..	Y	-.--
# M	--	Z	--..
morse_code_dict = {"A":	".-", "N": "-.", "B":	"-...", "O":	"---", "C":	"-.-.", "P":	".--.",
                   "D":	"-..",	"Q":	"--.-", "E":	".",	'R':	'.-.', 'F':	'..-.',	'S':	'...', 'G':	'--.',
                   'T':	'-', 'H':	'....',	'U':	'..-', 'I':	'..',	'V':	'...-', 'J':	'.---',	'W':	'.--',
                   'K':	'-.-',	'X':	'-..-', 'L':	'.-..',	'Y':	'-.--', 'M':	'--',	'Z':	'--..'}

def decoding_character(morse_character):
    for keys, values in morse_code_dict.items():
        if values == morse_character:
            return keys

def decoding(morse):
    result = ''
    for i in range(len(morse)):
        if morse[i] == '':
            result += ' '
        else:
            result += decoding_character(morse[i])
    return(result)

line = input("모스 부호를 입력하세요 : ").split(" ")
print(decoding(line))

# 5. ngram 기반 두 문장 유사도 구하기(n=2, 3)
str1 = "오늘 멀티캠퍼스에서 너무 쉬운 프로그래밍을 공부했다"
str2 = "멀티캠퍼스에서 공부했던 오늘의 프로그래밍은 너무 쉬웠다"
def similarity(str1, str2):
    str11 = str1.replace(" ", "")
    str21 = str2.replace(" ", "")
    s1 = {str11[i:i+2] for i in range(len(str11)-1)}
    s2 = {str21[i:i+2] for i in range(len(str21)-1)}
    if len(s1) >= len(s2):
        print((len(s1 & s2)/len(s1)) * 100, "%의 유사도를 보입니다.")
    else:
        print((len(s1 & s2)/len(s2)) * 100, "%의 유사도를 보입니다.")

similarity(str1, str2)

