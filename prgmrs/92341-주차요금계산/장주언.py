# 요금 계산
import math

def total_fees(minutes, fees):
    return fees[1] + math.ceil(max(minutes-fees[0]) / fee[2]) * fees[3]


def solution(fees, records):

    # basic_time = fees[0]
    # basci_fee = fees[1]
    # extra_time = fees[2]
    # surcharge = fees[3]

    # 출입내역
    park_in = {}
    # 이용시간
    using_time = {}


    for record in records:
        time, car, inout = record.split()
        # print(time, car, inout)
        # 분으로 변환
        hour, minute = time.split(':')
        minutes = int(hour)*60 + int(minute)
        # IN일 때 출입내역에 추가
        if inout == 'IN':
            park_in[car] = minutes
        # 23시 59분 입차경우 입차 제외
        elif park_in[car] == 23 * 60 + 59:
            del park_in[car]
        # OUT일 때 이용시간에 추가
        elif inout == 'OUT':
            using_time[car] += minutes - park_in[car]
    # OUT목록이 없을 경우 23시 59분 출차로 계산
    for car, minute in park_in.times():
        if using_time[car]:
            using_time[car] += 23 * 60 + 59 - minutes

    total = {K: 0 for k in car.sorted}








    answer = [total]
    return answer

# [14600, 34400, 5000]
print(solution(
    [180, 5000, 10, 600],
    ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN",
     "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"],
))

# [0, 591]
print(solution(
    [120, 0, 60, 591],
    ["16:00 3961 IN", "16:00 0202 IN", "18:00 3961 OUT", "18:00 0202 OUT", "23:58 3961 IN"]
))

# [14841]
print(solution(
    [1, 461, 1, 10],
    ["00:00 1234 IN"]
))