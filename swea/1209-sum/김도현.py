import sys
sys.stdin = open('input.txt')

for t in range(1, 11):
    t = int(input())

    bae_yul = []
    for n in range(100):
        bae_yul.append(list(map(int, input().split())))
    # print(bae_yul)
    max_row = sum(bae_yul[0])
    dae_sum = 0
    ban_dae_sum = 0
    for idx in range(len(bae_yul)):
        current_row_sum = sum(bae_yul[idx])
        if current_row_sum >= max_row:
            max_row = current_row_sum
        dae_sum += bae_yul[idx][idx]
        ban_dae_sum += bae_yul[-idx-1][-idx-1]

    zip_bae_yul = list(map(list, zip(*bae_yul)))
    max_column = sum(zip_bae_yul[0])
    for idx in range(len(zip_bae_yul)):
        current_column_sum = sum(zip_bae_yul[idx])
        if current_column_sum >= max_column:
            max_column = current_column_sum
    # print(bae_yul, zip_bae_yul)
    # print(f'{max_row}, {dae_sum}, {ban_dae_sum}, {max_column}')

    total_max = max(max_row, max_column, dae_sum, ban_dae_sum)

    print(f'#{t} {total_max}')

    # 가로 세로 좌표로 풀기
    # 이렇게 하면 for 문 2번으로 sum 4개를 다 구할 수 있음. 가장 심플한 방법입니다. 인덱스 구하기 잘 합시다.
    N = 100
    row_max = col_max = 0

    diag_sum1 = diag_sum2 = 0

    for a in range(N):
        # 행합, 열합, 대각선1합, 대각선2합
        row_sum = col_sum = 0

        for b in range(N):
            row_sum += bae_yul[a][b]
            col_sum += bae_yul[b][a]

        # b for문 안으로 들어가면 10000번 돌지만, 여기있으면 값은 같으면서 100번만 돌아감.
        diag_sum1 += bae_yul[a][a]
        diag_sum2 += bae_yul[a][N-a-1]

        if row_sum > row_max:
            row_max = row_sum


    # 전치행렬?