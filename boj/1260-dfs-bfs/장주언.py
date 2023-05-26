def dfs(V):
    pass
    # dfs의 경로를 보여줘
    # 방문여부
    visited = [False for _ in range(N+1)]
    # 방문할 곳들
    to_visit = [V]
    # 경로를 입력할 곳들
    route = []
    # 앞으로 방문 할 곳이 남을 때까지 반복
    while to_visit:
        # 현재 위치는 방문할 곳들 중 가장 마지막
        current = to_visit.pop()
        # 현재 위치가 visitied에 False: 면 True로 바꿔주고
        if not visited[current]:
            route.append(current)
            visited[current] = True
            # 방문할 곳들에 추가해주는데, 작은 수부터 볼 꺼니까 끝에서부터 꺼내서 리버스 소트
            to_visit += sorted(graph[current], reverse=True)

    return ' '.join(map(str, route))


def bfs(V):
    # dfs의 경로를 보여줘
    # 방문여부
    visited = [False for _ in range(N + 1)]
    # 방문할 곳들
    to_visit = [V]
    # 경로를 입력할 곳들
    route = []
    # 앞으로 방문 할 곳이 남을 때까지 반복
    while to_visit:
        # 현재 위치는 방문할 곳들 중 가장 마지막
        current = to_visit.pop(0)
        # 현재 위치가 visitied에 False: 면 True로 바꿔주고
        if not visited[current]:
            route.append(current)
            visited[current] = True
            # 방문할 곳들에 추가해주는데, 앞에서 부터 꺼내니까 소트
            to_visit += sorted(graph[current])
    return ' '.join(map(str, route))


N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):

    start, end = map(int, (input().split()))

    # graph 양 방향 채우기

    graph[start].append(end)
    graph[end].append(start)

print(dfs(V))
print(bfs(V))
