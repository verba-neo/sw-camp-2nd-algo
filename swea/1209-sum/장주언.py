import sys

sys.stdin = open('./input.txt')

T = 10
for tc in range(1, T + 1):
    int(input())

    N = 100

    numbers = [list(map(int, input().split())) for _ in range(N)]

    answer = dia1 = dia2 = 0

    for i in range(N):
        row = column = 0
        for j in range(N):
            row += numbers[i][j]
            column += numbers[j][i]
        answer = max(answer, row, column)

        dia1 += numbers[i][i]
        dia2 += numbers[i][N -1 - i]
    answer = max(answer, dia1, dia2)

    print(f'#{tc} {answer}')
