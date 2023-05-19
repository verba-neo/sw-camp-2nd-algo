import sys
sys.stdin = open(('./input.txt'))

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    number = list(map(int, input()))

    count = [0] * 10
    for cnt in number:
        count[int(cnt)] += 1

    max_num = 0
    idx_num = 0

    for cnt_max in range(len(count)):
        if max_num <= count[cnt_max]:
            max_num = count[cnt_max]
            idx_num = cnt_max

    print(f'#{tc} {idx_num} {max_num}')
