import sys
sys.stdin = open('./input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    snail_list = [[0] * N for _ in range(N)]

    # 초기값 [0, 0], 초기 입력값 = 1, -> 입력값 += 1 , 초기 방향값 = 0
    # 범위 밖이면 방향 전환
    # 이동한 방향의 값이 '0'이 아니면 방향 전환
    # 입력 값이 N ** 2 보다 같거나 작을 때까지

    de_x = [0, 1, 0, -1]
    de_y = [1, 0, -1, 0]

    x, y, cnt = 0, 0, 1
    snail_list[x][y] = 1
    direction = 0

    while cnt < N ** 2:
        move_x = x + de_x[direction]
        move_y = y + de_y[direction]

        if 0 <= move_x < N and 0 <= move_y < N and snail_list[move_x][move_y] == 0:
            x, y = move_x, move_y
            snail_list[x][y] = cnt
            cnt += 1
        else:
            direction = (direction + 1) % 4

    print(f'#{tc}')
    for i in snail_list:
        print(*i)
