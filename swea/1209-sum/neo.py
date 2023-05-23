import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    input()
    N = 100

    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 가로 최대/ 세로 최대
    row_max = col_max = 0

    # 대각1합   대각2합
    diag_sum1 = diag_sum2 = 0

    for a in range(N):
        # 행합    열합
        row_sum = col_sum = 0

        for b in range(N):
            # 행 우선 순회
            row_sum += matrix[a][b]
            # 열 우선 순회
            col_sum += matrix[b][a]

        # 정 대각 순회
        diag_sum1 += matrix[a][a]
        # 반 대각 순회
        diag_sum2 += matrix[a][N-a-1]

        # 지속적으로 행 최대 갱신
        if row_sum > row_max:
            row_max = row_sum
        # 지속적으로 열 최대 갱신
        if col_sum > col_max:
            col_max = col_sum

    # 대각선 최대 갱신
    diag_max = diag_sum1 if diag_sum1 > diag_sum2 else diag_sum2

    ans = max(row_max, col_max, diag_max)
    print(f'#{tc} {ans}')
