import sys
sys.stdin = open('./input.txt')

# T = int(input())
T = 10

for tc in range(1, T+1):
    N = 100
    test_case = int(input())
    game_board = [list(map(int, input().split())) for _ in range(N)]

    end_row = N-1
    end_col = 0

    d_rows = [0, 0, 1]
    d_cols = [-1, 1, 0]

    direction = 0

    for dep_idx in range(N):
        if game_board[N-1][dep_idx] == 2:
            end_col += dep_idx

    while end_row != 0:
        # 오른쪽 방향 으로 '1'이 계속 있으면 while 문으로 계속 이동
        if 0 <= end_col + 1 < N and game_board[end_row][end_col+1] == 1:
            while end_col + 1 < N and game_board[end_row][end_col+1]:
                end_col += 1
            end_row -= 1
        # 왼쪽 방향 이동
        elif 0 <= end_col - 1 < N and game_board[end_row][end_col-1] == 1:
            while end_col - 1 < N and game_board[end_row][end_col-1]:
                end_col -= 1
            end_row -= 1
        # 두 방향 다 없으면 위로 이동
        else:
            end_row -= 1

    print(f'#{tc} {end_col}')
