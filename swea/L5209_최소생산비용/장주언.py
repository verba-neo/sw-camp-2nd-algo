import sys

sys.stdin = open('./input.txt')


def dfs(product, product_cost):
    global answer

    if product_cost > answer:
        return
    if product == N:

        if answer > product_cost:
            answer = product_cost
            return

    for factory in range(N):
        if not factory_visited[factory]:
            factory_visited[factory] = True
            dfs(product+1, product_cost+matrix[product][factory])
            factory_visited[factory] = False


T = int(input())

for tc in range(1, T+1):

    N = int(input())

    matrix = [list(map(int, input().split())) for _ in range(N)]

    answer = 99 * N

    factory_visited = [False for _ in range(N)]

    dfs(0, 0)

    print(f'#{tc} {answer}')