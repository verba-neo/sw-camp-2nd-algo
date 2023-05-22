import sys
sys.stdin = open('./input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input()))

    # 카드 개수 세기
    count = [0] * 10
    # count = {k: 0 for k in range(10)}

    for cnt in numbers:
        count[cnt] += 1

    max_count = 0
    idx_num = 0

    for cnt_max in range(len(count)):
        if max_count <= count[cnt_max]:
            max_count = count[cnt_max]
            idx_num = cnt_max

    print(f'#{tc} {idx_num} {max_count}')
