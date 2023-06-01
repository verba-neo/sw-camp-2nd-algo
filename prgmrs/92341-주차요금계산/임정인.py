from math import ceil


def time2price(t, defaulttime, defaultprice, unittime, unitprice):
    # 기본시간 이하이면 기본요금 청구
    if t <= defaulttime:
        return defaultprice
    # 초과한 시간에 대해서 단위 시간마다 단위 요금을 청구
    excesstime_unit = ceil((t - defaulttime) / unittime)
    return defaultprice + excesstime_unit * unitprice


def h2m(t):
    # 시간 문자열을 분 단위 정수 값으로 바꾸기
    return 60 * int(t.split(':')[0]) + int(t.split(':')[1])


def solution(fees, records):
    # 주차장에 들어와있는 차들의 상태를 관리하는 state 딕셔너리 만들기
    # 각 차별로 누적 시간을 나타내는 car2time 딕셔너리 만들기
    state, car2time = {}, {}

    for record in records:
        time, car, type = record.split();
        time = h2m(time)
        if type == 'IN':
            # 입차 시간을 기록
            state[car] = time
        else:
            # 현재 해당 차의 누적 주차 시간에
            # 입차 시간과 출차 시간의 차이 더하기
            car2time[car] = car2time.get(car, 0) + (time - state[car])
            state.pop(car)

    # 아직 주차되어 있는 차는 23:59에 출차된 것으로 간주
    for car, time in state.items():
        car2time[car] = car2time.get(car, 0) + (h2m('23:59') - time)

    car2price = {car: time2price(time, *fees) for car, time in car2time.items()}

    answer = [car2price[car] for car in sorted(car2price.keys())]
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