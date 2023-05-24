# 사다리 타기
# 갈 수 있는 방향은 1로 표시, 못 가면 0
# 100 x 100의 크기
# 도착지점은 2
# 도착지점으로 갈 수 있는 출발점 x 구하기

import sys

sys.stdin = open('./input.txt')

T = 10

for tc in range(1, T + 1):

    input()

    ladders = list(list(map(int, input().split())) for _ in range(100))
    # 도착지점 찾기


    # 도착지점의 index = [99][col]

    # 도착 지점을 알기 때문에 거꾸로 올라간다.
    # 사다리타기는 좌,우가 상하보다 우선권이 있으므로 좌우상으로 설정
    d_rows = [0, 0, -1]
    d_col = [-1, 1, 0]
    directions = 0

    row = 99
    col = ladders[99].index(2)

    # 새로운 row 값이 0이 될 때까지
    while row != 0:

        nr = row + d_rows[directions]
        nc = col + d_col[directions]
        # nr과 nc가 100x100의 범위 안에있고  ladders[nr][nc]가 1일 경우에
        if 0 <= nr < 100 and 0 <= nc < 100 and ladders[nr][nc]:
            # 이미 지나간 자리는 0으로 바꿔주고
            ladders[nr][nc] = 0
            # row와 col의 값을 바꿔준후
            row = nr
            col = nc
            # 자리에서 다시 탐색 해야하므로 초기화
            directions = 0

        else:
            directions = (directions + 1) % 3

    print(f'#{tc} {col}')











