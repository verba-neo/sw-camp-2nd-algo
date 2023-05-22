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
