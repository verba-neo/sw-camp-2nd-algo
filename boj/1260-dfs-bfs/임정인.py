from _collections import deque

def dfs(start):
    visited[start] = True
    print(start, end = '')

    for i in graph[start]:
        if not visited[i]:
            dfs(i)

def bfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:

        v = queue.popleft()
        print(v, end = '')
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 정렬
for i in graph:
    i.sort()

# dfs
visited = [False] * (N+1)
dfs(V)
print()

#bfs
visited = [False] * (N+1)
bfs(V)



# 강사님 답안

def dfs():  # 뒤에서부터 방문
    visited =[False for _ in range(N+1)]
    to_visits = [V]
    history = []  # 방문 순서 (방문 기록)

    while to_visits:
        current = to_visits.pop()
        if not visited[current]:
            visited[current] = True
            history.append(current)
            to_visits += sorted(graph[current], reverse=True)  # 내림차순 4 3 2

    return history

# .sort(메서드) : return 없이 기존 값 변경
# sorted() : 함수, 기존 값 변경 후 return


def bfs():
    visited = [False for _ in range(N + 1)]
    to_visits = [V]
    history = []

    while to_visits:
        current = to_visits.pop()
        if not visited[current]:
            visited[current] = True
            history.append(current)
            to_visits += sorted(graph[current])  # 오름차순

    return history


# 정점, 간선, 시작점
N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]  # 0 지울거니까 0 다음거까지 해서 N+1


for _ in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

# print(graph)  그래프 완성

print(*dfs())
print(*bfs())
