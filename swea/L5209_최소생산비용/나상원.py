import sys
sys.stdin = open('./input.txt')

T = int(input())


def dfs(depth):
    global product_cost, total_cost

    if depth == N:
        product_cost = min(product_cost, total_cost)
        return

    if product_cost < total_cost:
        return

    for nxt in range(N):
        if not visited[nxt]:
            visited[nxt] = True
            total_cost += factory[depth][nxt]
            dfs(depth+1)
            visited[nxt] = False
            total_cost -= factory[depth][nxt]


for tc in range(1, T+1):
    N = int(input())
    factory = [list(map(int, input().split())) for _ in range(N)]

    visited = [False for _ in range(N)]
    product_cost = 987654321
    total_cost = 0

    dfs(0)

    print(f'#{tc} {product_cost}')

