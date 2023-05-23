import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):

    N = int(input())
    building = list(map(int, input().split()))

    good_view = 0
    for idx in range(2, N-2):
        current_b = building[idx]
        left_max = max(building[idx-2:idx])
        right_max = max(building[idx+1: idx+2 +1])
        arround_max = max(left_max, right_max)
        # print(current_b, arround_max)
        if arround_max < current_b:
            good_view += current_b - arround_max

    print(f'#{t} {good_view}')
