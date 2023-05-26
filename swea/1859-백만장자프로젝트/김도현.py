import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):

    answer = 0
    days = int(input())
    total_price_list = list(map(int, input().split()))

    # # 10개 중에 9개 맞고 runtime error
    # idx = 0
    # while idx < len(total_price_list) -1:
    #     price_list = total_price_list[idx:]
    #     # print(price_list)
    #     highest_day = price_list.index(max(price_list))
    #     print(t, idx)
    #     if highest_day != 0:
    #         for i in range(highest_day+1):
    #             if price_list[i] < price_list[highest_day]:
    #                 answer += price_list[highest_day] - price_list[i]
    #             else:
    #                 idx += highest_day + 1
    #                 break
    #             # idx += 1
    #     else:
    #         idx += 1

    # # 10개 중에 6개 맞고 제한시간 초과
    # idx = 0
    # while idx < days:
    #     highest_v = max(total_price_list[idx:])
    #     if total_price_list[idx] >= highest_v:
    #         idx += 1
    #     else:
    #         answer += highest_v - total_price_list[idx]
    #         idx += 1

    # 퉤





    print(f'#{t} {answer}')
