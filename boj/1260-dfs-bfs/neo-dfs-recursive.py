def dfs(v):
    visited[v] = True
    history.append(v)

    for new_v in graph[v]:
        if not visited[new_v]:
            dfs(new_v)


# 정점, 간선, 시작점
N, M, V = map(int, input().split())

visited = [False for _ in range(N+1)]
history = []
graph = [[] for _ in range(N+1)]

for _ in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

for to_go in graph:
    to_go.sort()

dfs(V)

print(*history)
