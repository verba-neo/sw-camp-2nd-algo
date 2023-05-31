import math


# recodes 에 시간이 ':'로 되 있어서 기준 으로 split() 구분, 시간을 분으로 바꿔 줘야함
def change_time(time):
    h, m = map(int, time.split(':'))

    return 60*h + m


def solution(f, re):
    answer = []

    recodes_dic = {}
    total_fee = {}

    for record in re:
        # 문자열 로 들어온 값들을 시간, 차 번호, 입출 여부 구분
        time, c_number, io = record.split()
        
        # 차 번호가 없으면 시간/ 차 번호를 키 값으로 리스트 [시간, 입출 여부] 추가
        if c_number not in recodes_dic:
            # 리스트 로 초기화
            recodes_dic[c_number] = [[time, io]]
        else:
            recodes_dic[c_number].append([time, io])
    # print(records_dic)

    # 총 시간 / 총 주차 요금 계산
    for recode in recodes_dic:
        total_time = 0
        fee = f[1]
        # 차 번호에 대한 리스트 [시간, 입출 여부]의 개수가 홀수면 입차만 하고 출차는 없으니 ['23:59', 'OUT'] 추가
        if len(recodes_dic[recode]) % 2 != 0:
            recodes_dic[recode].append(['23:59', 'OUT'])
        # 입차 출차에 따라 총 시간을 계산
        for time_and_io in recodes_dic[recode]:
            if time_and_io[1] == 'IN':
                total_time -= change_time(time_and_io[0])
            else:
                total_time += change_time(time_and_io[0])
        
        # 총 시간이 입력된 최소 시간 보다 크면, 
        if total_time > f[0]:
            fee += math.ceil((total_time - f[0]) / f[2]) * f[3]
        # 아니면 기본 요금
        else:
            fee = f[1]

        total_fee[recode] = fee
    # 차 번호[key 값]에 따라 가장 작은 수 부터 정렬
    total_fee = sorted(total_fee.items())

    for car, fee in total_fee:
        answer.append(fee)

    return answer


fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
print(solution(fees, records))
