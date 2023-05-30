import sys
sys.stdin = open('./input.txt')

T = int(input())


def paper_cnt(num):
    count = 0

    # cnt 1 count 1
    # cnt 2 count 3
    # cnt 3 count 5
    # cnt 4 count 11
    # cnt 5 count 21

    if num == 1:
        count = 1
    elif num == 2:
        count = 3
    else:
        count = paper_cnt(num-1) + paper_cnt(num-2)*2

    return count


for tc in range(1, T+1):
    N = int(input())
    cnt = N // 10
    # 재귀
    print(f'#{tc} {paper_cnt(cnt)}')
