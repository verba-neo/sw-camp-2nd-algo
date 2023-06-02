import sys
sys.stdin = open('input.txt')


def dfs(row, col, total):
    global minimum
    # 가지치기(Pruning)
    if total > minimum:
        return
    # 마지막 칸 도달
    if row == N-1 and col == N-1:
        minimum = min(total, minimum)
        return

    for idx in range(2):
        new_r, new_c = row + drows[idx], col + dcols[idx]
        if new_r < N and new_c < N:
            new_total = total + matrix[new_r][new_c]
            dfs(new_r, new_c, new_total)


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    drows = [1, 0]
    dcols = [0, 1]
    minimum = float('inf')

    dfs(0, 0, matrix[0][0])
    print(f'#{tc} {minimum}')
