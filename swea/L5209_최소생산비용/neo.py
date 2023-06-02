import sys
sys.stdin = open('input.txt')


def dfs(product_idx, total):
    global minimum
    if product_idx == N:
        if total < minimum:
            minimum = total
        return

    for factory_idx in range(N):
        if not visited[factory_idx]:
            visited[factory_idx] = True
            new_total = total + matrix[product_idx][factory_idx]
            if new_total < minimum:  # backtracking
                dfs(product_idx+1, new_total)
            visited[factory_idx] = False


T = int(input())
for tc in range(1, T+1):
    minimum = float('INF')
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = [False for _ in range(N)]
    dfs(0, 0)

    print(f'#{tc} {minimum}')