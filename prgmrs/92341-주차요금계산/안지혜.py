import math


def solution(fees, records):
    # 차별로 누적 시간 구하기
    car_with_time = {}
    temp = {}
    for record in records:
        t, car_num, in_or_out = record.split()
        h, m = map(int, t.split(':'))
        h *= 60
        t = h + m

        if in_or_out == 'IN':
            temp.setdefault(car_num, t)
        else:
            if car_with_time.get(car_num):
                car_with_time[car_num] += t - temp[car_num]
            else:
                car_with_time.setdefault(car_num, t - temp[car_num])
            temp.pop(car_num)

    # 출차 안한 경우에 대한 누적 시간 계산
    if temp:
        max_time = 1439  # '23:59'
        for car_num in temp:
            if car_with_time.get(car_num):
                car_with_time[car_num] += max_time - temp[car_num]
            else:
                car_with_time.setdefault(car_num, max_time - temp[car_num])

    # 누적 시간에 대한 주차 요금 계산
    car_with_fee = {}
    for car_num, t in car_with_time.items():
        default_time, default_fee, additional_time, additional_fee = fees
        if t <= default_time:
            car_with_fee.setdefault(int(car_num), default_fee)
        else:
            total_fee = default_fee + math.ceil((t - default_time) / additional_time) * additional_fee
            car_with_fee.setdefault(int(car_num), total_fee)

    # 차량 번호 작은 자동차 -> 번호 큰 자동차 순서로 청구 요금 출력
    sorted_dict = dict(sorted(car_with_fee.items()))
    answer = [val for val in sorted_dict.values()]

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