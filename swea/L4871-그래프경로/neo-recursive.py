import sys
sys.stdin = open('input.txt')


def dfs(current):
    visited[current] = True

    for next_v in graph[current]:
        if not visited[next_v]:
            dfs(next_v)


T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    # Adj List Graph
    graph = [[] for _ in range(V+1)]

    for _ in range(E):
        start, end = map(int, input().split())
        graph[start].append(end)

    S, G = map(int, input().split())

    visited = [False for _ in range(V+1)]

    dfs(S)

    print(f'#{tc} {int(visited[G])}')


