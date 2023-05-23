import sys
sys.stdin = open('./input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    puzzle_list = []

    puzzle_cnt = 0

    for puz in range(N):
        puzzle_list.append(list(map(int, input().split())))


    print(f'#{tc} {puzzle_cnt}')
