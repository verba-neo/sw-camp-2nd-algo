import sys
sys.stdin = open('./input.txt')

# T = int(input())
T = 10

for tc in range(1, T + 1):
    t = int(input())
    N = 100
    board = []
    for n in range(N):
        board.append(list(map(int, input().split())))

    max_row_sum = 0
    for row_idx in range(N):
        # 가로줄 합계
        row_sum = 0
        for col_idx in range(N):
            row_sum += board[row_idx][col_idx]
        if row_sum > max_row_sum:
            max_row_sum = row_sum

    max_col_sum = 0
    for col_idx in range(N):
        # 세로줄 합계
        col_sum = 0
        for row_idx in range(N):
            col_sum += board[row_idx][col_idx]
        if col_sum > max_col_sum:
            max_col_sum = col_sum

    # 대각선 합계, [0,0] 시작인 것과 [0, 99] 시작인 것
    max_dia_num = 0
    for col_row_idx in range(N):
        dia_num_1 = 0
        dia_num_2 = 0
        dia_num_1 += board[col_row_idx][col_row_idx]
        dia_num_2 += board[col_row_idx][N-1-col_row_idx]

        max_dia_num = max(dia_num_1, dia_num_2)

    answer = max(max_col_sum, max_row_sum, max_dia_num)

    print(f'#{t} {answer}')
