import sys
sys.stdin = open('./input.txt')

T = int(input())


def dfs(row, col):
    global path_sum, min_sum

    d_row = [0, 1]
    d_col = [1, 0]

    if min_sum < path_sum:
        return

    if row == N-1 and col == N-1:
        min_sum = min(path_sum, min_sum)
        # sum_list.append(path_sum)
        return

    for direction in range(2):
        new_r = row + d_row[direction]
        new_c = col + d_col[direction]

        if new_r < N and new_c < N and not visited[new_r][new_c]:
            visited[new_r][new_c] = True
            path_sum += board[new_r][new_c]
            dfs(new_r, new_c)
            visited[new_r][new_c] = False
            path_sum -= board[new_r][new_c]


for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    # print(board)

    visited = [[False]*N for _ in range(N)]
    path_sum = board[0][0]
    min_sum = 13*N
    sum_list = []

    dfs(0, 0)

    print(f'#{tc} {min_sum}')
    # print(f'#{tc} {min(sum_list)}')
