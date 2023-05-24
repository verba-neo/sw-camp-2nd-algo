import sys
sys.stdin = open('./input.txt')


for tc in range(1, 11):
    N = int(input())
    array = []

    for i in range(100):
        array.append(list(map(int, input().split())))  # 2차원 배열의 각 행 값

    # 가로줄의 합
    max_row = 0
    for i in range(100):
        sum_ans = 0
        for j in range(100):
            sum_ans += array[i][j]
        if sum_ans > max_row:
            max_row = sum_ans

    # 세로줄의 합
    max_col = 0
    for i in range(100):
        sum_ans = 0
        for j in range(100):
            sum_ans += array[j][i]
        if sum_ans > max_col:
            max_col = sum_ans

    # 대각선의 합
    max_diag = 0
    for i in range(100):
        sum_ans1 = sum_ans2 = 0
        sum_ans1 += array[i][i]
        sum_ans2 += array[i][99-i]
    if max(sum_ans1, sum_ans2) > max_diag:
        max_diag = max(sum_ans1, sum_ans2)

        ans = max(max_row, max_col, max_diag)

    print(f'#{tc} {ans}')


