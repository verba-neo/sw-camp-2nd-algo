import sys
sys.stdin = open('input.txt')

T = int(input())

dx = [1, 0]
dy = [0, 1]
direc = 0

from collections import deque

for t in range(1, T+1):

    answer = 0
    N = int(input())
    puzzle = [list(map(int, input().split())) for _ in range(N)]

    x, y = 0, 0
    total = puzzle[y][x]

    # 결과: 8/10 - 런타임 에러
    q = deque()
    q.append([x, y, total])
    min_total = float("INF")
    while q:
        print(min_total, q)
        x, y, total = q.popleft()

        if total > min_total:
            continue
        else:
            if x == N-1 and y == N-1 and total < min_total:
                min_total = total

            for i in range(2):
                new_x, new_y = x+dx[i], y+dy[i]
                if 0 <= new_x < N and 0 <= new_y < N:
                    if total+puzzle[new_y][new_x] < min_total:
                        q.append([new_x, new_y, total + puzzle[new_y][new_x]])

    print(f'#{t} {min_total}')
