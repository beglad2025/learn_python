# 1. 아마존 면접문제
# 특정시간을 입력(예:11:05:20)으로 주었을 때
# 그 시간에 총 몇 명이 사무실에 있었는지 알려주는 함수를 작성하시오.

logFile = """09:12:23 11:14:35
10:34:01 13:23:40
10:34:31 11:20:10"""

# 출퇴근시간 데이터 처리
a, b, c = [v.split(" ") for v in logFile.split("\n")]
peopleData = [[x.split(":") for x in a], [x.split(":") for x in b], [x.split(":") for x in c]]
# [[['09', '12', '23'], ['11', '14', '35']], [['10', '34', '01'], ['13', '23', '40']], [['10', '34', '31'], ['11', '20', '10']]]

def remainPeople(time):
    timeList = time.split(":")  # timeList = ['11', '05', '20']
    global peopleData  # 처리한 데이터(logFile에 있던 세 사람의 출퇴근 시간)
    count = 0
    for i in range(len(peopleData)):  # 주어진 세 사람의 데이터로 비교하기 위해
        # HH 단위 비교 : 출근 HH < 기준 HH < 퇴근 HH 일 때
        if int(peopleData[i][0][0]) < int(timeList[0]) and int(timeList[0]) < int(peopleData[i][1][0]):
            count += 1
        # HH 단위 비교 : 출근 HH == 기준 HH 일 때
        elif int(peopleData[i][0][0]) == int(timeList[0]):
            for j in range(1, 3):  # j = 1일 때, MM 단위 비교 / j = 2일 때, SS 단위 비교
                if int(peopleData[i][0][j]) < int(timeList[j]):
                    count += 1
                    break
        # HH 단위 비교 : 기준 HH = 퇴근 HH 일 때
        elif int(timeList[0]) == int(peopleData[i][1][0]):
            for j in range(1, 3):  # j = 1일 때, MM 단위 비교 / j = 2일 때, SS 단위 비교
                if int(peopleData[i][1][j]) > int(timeList[j]):
                    count += 1
                    break
    return count

x = input("기준 시간을 HH:MM:SS 형식으로 입력하세요 : ")
print(remainPeople(x))

