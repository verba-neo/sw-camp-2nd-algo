import math


def change_time(time):
    h, m = map(int, time.split(':'))

    return 60*h + m


def solution(f, re):
    answer = []

    recodes_dic = {}
    to_fee = {}

    for record in re:
        time, c_number, io = record.split()

        if c_number not in recodes_dic:
            recodes_dic[c_number] = [[time, io]]
        else:
            recodes_dic[c_number].append([time, io])
    # print(records_dic)

    for recode in recodes_dic:
        to_time = 0
        fee = fees[1]

        if len(recodes_dic[recode]) % 2 != 0:
            recodes_dic[recode].append(['23:59', 'OUT'])

        for io in recodes_dic[recode]:
            if io[1] == 'IN':
                to_time -= change_time(io[0])
            else:
                to_time += change_time(io[0])

        if to_time > fees[0]:
            fee += math.ceil((to_time - fees[0]) / fees[2]) * fees[3]

        to_fee[recode] = fee
    to_fee = sorted(to_fee.items())

    for c, f in to_fee:
        answer.append(f)

    return answer


fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
print(solution(fees, records))
