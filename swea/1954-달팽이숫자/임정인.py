import sys
sys.stdin = open('./input.txt')

# 테스트 데이터 개수
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    board = [[0] * N for _ in range(N)]  # [0]*N 개 있는게 N줄

    d_rows = [0, 1, 0, -1]
    d_cols = [1, 0, -1, 0]
    # 0:하, 1:우, 2:상, 3:좌
    direction = 0  # idx

    # 행/열 좌표값 (시작하는 좌표 값), 마지막으로 채운 곳
    row = col = 0
    # 채워 나갈 숫자
    num = 1
    board[0][0] = num

    while num != N**2:
        # 새로운 row/col 좌표값
        n_row = row + d_rows[direction]
        n_col = col + d_cols[direction]
        # 새로운 좌표값은 0이상 N미만이며, 숫자가 채워져 있지 않아야 한다 (0)
        # 0 이 아닌 다른 숫자가 들어있다면 방향을 꺾어야 한다
        if 0 <= n_row < N and 0 <= n_col< N and not board[n_row][n_col]:
            num += 1
            board[n_row][n_col] = num
            row, col = n_row, n_col
        else:
            # 진입할 수 없다면 direction 고치기
            # [0,1] -> [1,0] -> [0, -1] -> [-1,0] 순서
            direction = (direction + 1) % 4

    # 함수 실행할 때 * 붙이면 겉에 있는 괄호 제거 가능
    print(f'#{tc}')
    for i in range(N):
        print(*board[i])
