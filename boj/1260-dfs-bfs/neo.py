def dfs():
    visited = [False for _ in range(N+1)]
    to_visits = [V]
    # 방문 기록
    history = []

    while to_visits:
        current = to_visits.pop()
        if not visited[current]:
            visited[current] = True
            history.append(current)
            # 작은것부터 방문 => pop() 이므로 뒤에서부터 나옴 => 내림차순 정렬 필요
            to_visits += sorted(graph[current], reverse=True)
    return history


def bfs():
    visited = [False for _ in range(N+1)]
    to_visits = [V]
    history = []

    while to_visits:
        current = to_visits.pop(0)
        if not visited[current]:
            visited[current] = True
            history.append(current)
            # 작은것부터 방문 => pop(0) 이므로 앞에서부터 나옴 => 오름차순 정렬 필요
            to_visits += sorted(graph[current])
    return history


# 정점, 간선, 시작점
N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)


print(*dfs())
print(*bfs())
