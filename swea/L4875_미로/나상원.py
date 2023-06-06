import sys
sys.stdin = open('./input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    miro = [list(map(int, input())) for _ in range(N)]

    r = c = 0
    for row in range(N):
        for col in range(N):
            if miro[row][col] == 2:
                r, c = row, col
                break

    positions = []
    visited = [[False]*N for _ in range(N)]
    # 시작 위치
    positions.append([r, c])
    # 방문
    visited[r][c] = True

    answer = 0

    d_row = [0, 1, 0, -1]
    d_col = [1, 0, -1, 0]

    while positions:
        cur_r, cur_c = positions[-1]

        if miro[cur_r][cur_c] == 3:
            answer = 1
            break

        for move in range(4):
            new_r = cur_r + d_row[move]
            new_c = cur_c + d_col[move]

            if 0 <= new_r < N and 0 <= new_c < N and miro[new_r][new_c] != 1 and not visited[new_r][new_c]:
                positions.append((new_r, new_c))
                visited[new_r][new_c] = True
                break
        else:
            positions.pop()

    print(f'#{tc} {answer}')
