import sys
sys.stdin = open('./input.txt')

# T = int(start())
T = 10

for tc in range(1, T + 1):
    t = int(input())
    board = []
    for n in range(100):
        board.append(list(map(int, input().split())))

    max_col_sum = 0
    for row_idx in range(100):
        col_sum = 0
        for col_idx in range(100):
            col_sum += board[row_idx][col_idx]
        if col_sum > max_col_sum:
            max_col_sum = col_sum

    max_row_sum = 0
    for col_idx in range(100):
        row_sum = 0
        for row_idx in range(100):
            row_sum += board[row_idx][col_idx]
        if row_sum > max_row_sum:
            max_row_sum = row_sum

    dia_num_1 = 0
    dia_num_2 = 0
    max_dia_num = 0
    for col_row_idx in range(100):
        dia_num_1 += board[col_row_idx][col_row_idx]
        dia_num_2 += board[col_row_idx][99 - col_row_idx]
    max_dia_num = max(dia_num_1, dia_num_2)

    answer = max(max_col_sum, max_row_sum, max_dia_num)

    print(f'#{t} {answer}')
