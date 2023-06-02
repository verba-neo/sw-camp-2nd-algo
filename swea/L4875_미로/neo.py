import sys
sys.stdin = open('input.txt')


drs = [-1, 1, 0, 0]
dcs = [0, 0, -1, 1]


def dfs(row, col):
    global answer

    # 답을 찾았다면 함수 종료
    if answer == 1:
        return

    for idx in range(4):

        new_row = row + drs[idx]
        new_col = col + dcs[idx]
        if 0 <= new_row < N and 0 <= new_col < N and not visited[new_row][new_col]:
            # 도착지점 => 종료 플래그
            if graph[new_row][new_col] == 3:
                answer = 1
                return
            # 벽이 아닌 길 => 방문처리 후 이동(dfs)
            elif graph[new_row][new_col] == 0:
                visited[new_row][new_col] = True
                dfs(new_row, new_col)


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