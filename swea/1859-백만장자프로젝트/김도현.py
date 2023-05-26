import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):

    answer = 0
    # days = int(start())
    # total_price_list = list(map(int, start().split()))
    # idx = 0
    # while idx < len(total_price_list):
    #     price_list = total_price_list[idx:]
    #     # print(price_list)
    #     highest_day = price_list.index(max(price_list))
    #     print(idx)
    #     if highest_day != 0:
    #         for i in range(highest_day+1):
    #             if price_list[i] < price_list[highest_day]:
    #                 answer += price_list[highest_day] - price_list[i]
    #             else:
    #                 idx += 1
    #                 break
    #             idx = highest_day+1
    #     else:
    #         idx += 1
    # ??? idx 조절을 해봅시다.


    print(f'#{t} {answer}')
