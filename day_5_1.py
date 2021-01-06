# 1. a 리스트에서 중복 숫자를 제거해 보자.
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
# 다른 방법
b = []
for x in a:
    if not x in b:
        b.append(x)
print(b)

# 3. while문을 사용하여 다음과 같이 별(*)을 표시하는 프로그램을 작성해 보자.
# 이중 for문으로 작성해 다시 해보기
# 2)
#      *
#     **
#    ***
#   ****
#  *****

c = '*'
for i in range(5):
    for j in range():
        print(" ")
    for k in range(??):
        print('*')

# 3)adv
#      *
#     ***
#    *****
#   *******
#  *********
