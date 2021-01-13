emails = ['python@mail.example.com', 'python+kr@example.com', #올바른 형식
          'python-dojang@example.co.kr', 'python_10@example.info', #올바른 형식
          'python.dojang@e-xample.com', #올바른 형식
          '@example.com', 'python@example', 'python@example-com'] #잘못된 형식
import re
def email_form(email_list):
    for i in range(len(email_list)):
        res = re.match("[\w\W.-]+[@][\w\W.-]+[.][\w\W.-]+", email_list[i])
        if res == None:
            email_list[i] += " -잘못된 형식"
        else:
            email_list[i] += " -올바른 방식"
    print(email_list)
# 확인
email_form(emails)



import re
print(re.match("\d{4}", "1234"))
# <re.Match object; span=(0, 4), match='1234'>
print(re.match("\d{4}", "1234"))
# <re.Match object; span=(0, 4), match='1234'>
# 4자리가 아니라 5자리로 되어있는데도 매치되는 것으로 나온다

if re.match("\d{4}", "12345"):
    print("정상 전화번호")
else:
    print("비정상 전화번호")
# if문에 활용하는 경우, 매치가 되기 때문에 정상 전화번호로 출력된다.
# 이런 경우
if re.match("\d{4}$", "12345"):  # $기호를 써서 '마지막에 꼭 4글자로 끝났으면 좋겠다'라고 설정하면된다.
    print("정상 전화번호")
else:
    print("비정상 전화번호")
# 비정상 전화번호로 출력됨

