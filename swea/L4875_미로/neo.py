import sys
sys.stdin = open('input.txt')


def dfs(row, col):
    global answer

    if answer == 1:
        return

    if graph[row][col] == 3:
        answer = 1
        return

    visited[row][col] = True

    for idx in range(4):
        new_row = row + drs[idx]
        new_col = col + dcs[idx]
        if 0 <= new_row < N and 0 <= new_col < N and not visited[new_row][new_col]:
            # 벽이 아닌 길 => 방문처리 후 이동(dfs)
            if graph[new_row][new_col] != 1:
                dfs(new_row, new_col)


drs = [-1, 1, 0, 0]
dcs = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    graph = [list(map(int, list(input()))) for _ in range(N)]
    visited = [[False for _ in range(N)] for _ in range(N)]

    for r in range(N):
        for c in range(N):
            if graph[r][c] == 2:
                break

    answer = 0
    visited[r][c] = True
    dfs(r, c)
    print(f'#{tc} {answer}')