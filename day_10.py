# 1.0~9의 문자로 된 숫자를 입력받았을 때, 이 입력값이 0~9의 모든 숫자를
# 각각 한 번씩만 사용한 것인지 확인하는 함수를 작성하시오.
# 입력 예시: 0123456789 01234 01234567890 6789012345 012322456789
# 출력 예시: True False False True False
import re
def all_num(a):
    l1 = []
    for i in list(a):
        l1 += re.findall("[0-9]", i)
    l1.sort()
    l2 = list(set(l1))
    l2.sort()
    if l1 == l2:
        print("True")
    else:
        print("False")
a = input("숫자를 입력해주세요 : ")
all_num(a)

print("=" * 10)
# 2.
emails = ['python@mail.example.com', 'python+kr@example.com', #올바른 형식
          'python-dojang@example.co.kr', 'python_10@example.info', #올바른 형식
          'python.dojang@e-xample.com', #올바른 형식
          '@example.com', 'python@example', 'python@example-com'] #잘못된 형식
import re
def email_form(email_list):
    for i in range(len(email_list)):
        res = re.match("python[.+_-]*\w*[@](e-xample|mail|example)[.][a-z]+", email_list[i])
        if res == None:
            email_list[i] += " -잘못된 형식"
        else:
            email_list[i] += " -올바른 방식"
    print(email_list)
# 확인
email_form(emails)

print("=" * 10)
# 3.
news = """

연합뉴스TV
[날씨] 추위 대신 미세먼지 말썽…밤까지 중부 중심 눈
기사입력 2021.01.12. 오후 1:40 기사원문 스크랩 본문듣기  설정
화나요 후속기사원해요 좋아요 평가하기9 댓글9
글자 크기 변경하기
 인쇄하기
보내기
동영상 뉴스
[앵커]

오늘은 추위가 풀리는 대신 서쪽 지역의 공기 질이 나쁘겠습니다.

중부지방을 중심으로 눈도 내리겠습니다.

기상캐스터 연결해서 날씨 정보 더 자세히 알아보겠습니다.

김민지 캐스터.

[캐스터]

네, 추위가 한층 풀렸습니다.

어제보다 옷차림을 조금 더 가볍게 하고 나왔는데도 크게 춥지 않습니다.

내륙에 내려졌던 한파특보는 모두 해제가 됐고요.

오늘 한낮에 전국에 영상권으로 올라서겠습니다.

한낮에 서울은 1도, 대전 3도, 대구 5도 등 어제보다 5도 정도 기온이 높겠습니다.

따뜻한 서풍이 불어오면서 추위의 힘이 약해지는 건데요.

이 서풍을 타고 또 미세먼지가 들어오겠습니다.

대기 정체로 먼지가 쌓이면서 오늘은 서쪽 지역을 중심으로 미세먼지 농도 나쁨 수준 보이겠고요.

밤에 중국발 오염물질까지 들어와서 내일은 전국적으로 공기 질 상황이 나쁘겠습니다.

오늘 전국에 구름이 많습니다.

차츰 중부를 중심으로 눈이 내리겠습니다.

수도권과 충남, 전북에 1~3cm, 강원 영서와 충북, 경북과 제주 산지에 최고 5cm의 눈이 내려 쌓이겠습니다.

대부분 오늘 밤이면 그칠 텐데요.

강원 영서 지역은 내일 새벽까지 눈이 이어지겠습니다.

지금은 눈발 정도만 날리고 있습니다.

눈이 쌓이면서 퇴근길 무렵에는 길이 많이 미끄럽겠습니다.

조심히 이동하시기 바랍니다.

날씨 전해 드렸습니다.
"""
print("=" * 10)
# 1)[캐스터]가 캐스팅한 내용만 추출하시오
# 방법1
import re
caster = list(re.finditer("\[캐스터\]", news))
caster += list(re.finditer("날씨 전해 드렸습니다.", news))
caster_index = []
for i in range(len(caster)):
     a = caster[i].end()
     caster_index.append(a)
print(news[caster_index[0]+1:caster_index[1]])

# 방법2
print(re.search("\[캐스터\]", news))
print(re.search("날씨 전해 드렸습니다.", news))
# 실행 결과,
# 시작 : 246부터 251까지
# 끝 : 807부터 818까지
print(news[252:819])

print("=" * 10)
# 2)달린 댓글의 개수를 출력하시오
# 방법1
comment1 = re.finditer("댓글\d+", news)
for i in comment1:
    a = i.start()
    b = i.end()
print(news[a:b]+"개")

# 방법2
comment2 = re.finditer("댓글\d+", news)
for i in comment2:
    print(i.group()+"개")

# 방법3
print(re.search("댓글\d+", news))
# 실행 결과,
# 105부터 108까지
print(news[105:108]+"개")

print("=" * 10)
# 3)대전의 온도를 출력하시오
tem_dj = re.finditer("대전\s\d+도", news)
for i in tem_dj:
    print(i.group())

print("=" * 10)
# 4)가장 많이 등장한 단어가 무엇인가요?
list_news = news.split()
list_remove_duplicate_news = list(set(list_news))
for i in list_remove_duplicate_news:
    list_news.remove(i)  # list_news에는 한 번 이상 등장한 단어들만 남는다.

whole_news = news.split()
word_key_list = []
for i in list_news:
    x = whole_news.count(i)
    word_key_list.append(x)
word_dic = dict(zip(word_key_list, list_news))  # {중복 횟수 : 중복된 단어, ...} 형태의 dictionary 생성
print(word_dic[max(word_key_list)])  # 중복 횟수 list의 최댓값을 key로 하는 value를 출력

print("=" * 10)
# 5)가장 많이 등장한 글자는 무엇이며, 총 몇 번 등장했나요?
print({word: num for num, word in word_dic.items() if num == max(word_key_list)})
