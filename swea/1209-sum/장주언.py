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
            # 행과 열
            row += numbers[i][j]

            column += numbers[j][i]
            # 값 비교
        answer = max(answer, row, column)
        # 범위에 j의 영향을 받지 않는 대각 2개 좌대각 우대각
        dia1 += numbers[i][i]
        dia2 += numbers[i][N-1-i]
    # 행, 열 값과 또 비교
    answer = max(answer, dia1, dia2)

    print(f'#{tc} {answer}')
