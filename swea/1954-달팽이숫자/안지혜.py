import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    d_rows = [0, 1, 0, -1]
    d_cols = [1, 0, -1, 0]
    direction = 0

    board = [[0] * N for _ in range(N)]

    row = col = 0
    num = 1
    board[0][0] = num

    while num != N**2:
        nr = row + d_rows[direction]
        nc = col + d_cols[direction]

        if 0 <= nr < N and 0 <= nc < N and not board[nr][nc]:
            num += 1
            board[nr][nc] = num
            row, col = nr, nc
        else:
            direction = (direction + 1) % 4

    print(f'#{tc}')
    for i in range(N):
        print(*board[i])
