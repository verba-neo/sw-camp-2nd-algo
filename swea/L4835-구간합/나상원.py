import sys
sys.stdin = open('./input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr_list = list(map(int, input().split()))
    sum_list = []

    # max_sum = -float('INF')
    # min_sum = float('INF')

    for sum_cnt in range(N-M+1):
        total = 0
        sum_arr = 0

        for sum_idx in range(M):
            sum_arr += arr_list[sum_cnt + sum_idx]
        sum_list.append(sum_arr)

        # 더 할 때 마다 최대 / 최소를 갱신함.
        # end = sum_cnt + M
        # total = sum(arr_list[sum_cnt: end])

        # if total > max_sum:
        #     max_sum = total
        #
        # if total < min_sum:
        #     min_sum = total

        # answer = max_sum - min_sum
    # print(f'#{tc} {answer}')

    print(f'#{tc} {max(sum_list) - min(sum_list)}')
