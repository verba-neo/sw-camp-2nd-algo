import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    bus_stop_numbers = list(map(int, input().split()))

    # convert bus stop numbers to 0,1 list
    charging_spots = [0] * (N+1)
    for bus_stop in bus_stop_numbers:
        charging_spots[bus_stop] = 1

    # calc charging count until bus arrives at the last charging spot
    cur_position = 0
    charging_count = 0
    while cur_position < N-K:

        # if charging spots don't exist in K range, charging_count = 0
        if 1 not in charging_spots[cur_position+1:cur_position+K+1]:
            charging_count = 0
            break

        # search charging spots in K range
        for step in range(K, 0, -1):
            if charging_spots[cur_position+step] == 1:
                charging_count += 1
                cur_position += step
                break

    answer = charging_count

    print(f'#{tc} {answer}')
