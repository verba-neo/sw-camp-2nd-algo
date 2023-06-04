import sys
sys.stdin = open('input.txt')

D = ((0, -1), (0, 1), (-1, 0), (1, 0))


def dfs(row, col, s):
    if len(s) == 7:
        if s not in case:
            case.append(s)
        return

    for dx, dy in D:
        new_r, new_c = row + dx, col + dy

        if 0 <= new_r < 4 and 0 <= new_c < 4:
            dfs(new_r, new_c, s + arr[new_r][new_c])


for tc in range(1, int(input()) + 1):
    arr = [input().split() for _ in range(4)]
    case = []

    for i in range(4):
        for j in range(4):
            dfs(i, j, arr[i][j])

    print(f'#{tc}', len(case))
