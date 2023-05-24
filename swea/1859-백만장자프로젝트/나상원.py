import sys
sys.stdin = open('./input.txt')

T = int(input())

for tc in range(1, T+1):
    days = int(input())
    price = list(map(int, input().split()))

    benefit = 0
    max_pri = 0

    for pri in price[::-1]:
        if pri >= max_pri:
            max_pri = pri
        else:
            benefit += max_pri - pri

    print(f'#{tc} {benefit}')
