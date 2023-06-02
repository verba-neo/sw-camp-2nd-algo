import sys

sys.stdin = open('./input.txt')


def search(row, col):
    global answer, inspection
    # answer가 inspection보다 작으면 끝
    if answer < inspection:
        return
    # 도착지에 도달했을때 answer값 갱신
    if row == N - 1 and col == N - 1:
        answer = min(answer, inspection)

    # 방향은 하 우
    directions = [(1, 0), (0, 1)]
    for d_row, d_col in directions:

        nxt_row = row + d_row
        nxt_col = col + d_col
        # 범위안에 있을 경우 방문하지 않았다면
        if 0 <= nxt_row < N and 0 <= nxt_col < N and not visited[nxt_row][nxt_col]:
            # 방문처리
            visited[nxt_row][nxt_col] = True
            # inspection 값에 더해주고
            inspection += area[nxt_row][nxt_col]
            # 다시 돌린다
            search(nxt_row, nxt_col)
            # 돌리고 아니면 False 처리하고 나와서 다시 돌린다
            visited[nxt_row][nxt_col] = False
            # 더했던 값은 다시 빼주고
            inspection -= area[nxt_row][nxt_col]


T = int(input())

for tc in range(1, T+1):

    N = int(input())

    area = [list(map(int, input().split())) for _ in range(N)]

    answer = 10 * (2*N-1)

    inspection = area[0][0]

    visited = [[False for _ in range(N)] for _ in range(N)]

    search(0, 0)

    print(f'#{tc} {answer}')


