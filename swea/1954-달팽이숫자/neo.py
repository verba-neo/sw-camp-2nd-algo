import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    board = [[0] * N for _ in range(N)]

    d_rows = [0, 1, 0, -1]
    d_cols = [1, 0, -1, 0]
    direction = 0

    # 행/열 좌표값(마지막으로 채운 위치)
    row = col = 0
    # 채워 나갈 숫자
    num = 1
    board[0][0] = num

    while num != N**2:
        # 새로운 row/col 좌표값
        nr = row + d_rows[direction]
        nc = col + d_cols[direction]

        # 새로운 좌표값은 0이상 N미만이며, 숫자가 채워져 있지 않아야 한다 (0)
        if 0 <= nr < N and 0 <= nc < N and not board[nr][nc]:
            num += 1
            board[nr][nc] = num
            row, col = nr, nc
        else:
            direction = (direction + 1) % 4

    print(f'#{tc}')
    for i in range(N):
        print(*board[i])

