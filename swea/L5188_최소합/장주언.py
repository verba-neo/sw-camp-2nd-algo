import sys

sys.stdin = open('./input.txt')

T = int(input())

for tc in range(1, T+1):

    N = int(input())

    lst = [list(map(int, input().split())) for _ in range(N)]

    row, col = 0

    _sum = 0

    visited = []


def dfs(idx, total):

    # 오른쪽 혹은 아래
    directions = [(1, 0), (0, 1)]
    for d_row, d_col in directions:

        nxt_row = row + d_row
        nxt_col = col + d_col

        visited.apend(lst[nxt_row][nxt_col])



