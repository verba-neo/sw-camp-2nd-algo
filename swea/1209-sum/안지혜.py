import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    boxes = [list(map(int, input().split())) for _ in range(100)]

    max_val = 0
    for r in range(100):

        rows_sum_val = 0
        cols_sum_val = 0
        diagonal_sum_val = 0
        for c in range(100):
            rows_sum_val += boxes[r][c]
            cols_sum_val += boxes[c][r]
            diagonal_sum_val += boxes[c][c]

        if rows_sum_val > max_val:
            max_val = rows_sum_val

        if cols_sum_val > max_val:
            max_val = cols_sum_val

        if diagonal_sum_val > max_val:
            max_val = diagonal_sum_val

    answer = max_val

    print(f'#{tc} {answer}')