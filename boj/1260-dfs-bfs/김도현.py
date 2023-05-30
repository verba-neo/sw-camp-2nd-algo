N, M, V = map(int, input().split())

# 정점의 갯수만큼 만들기
graph = [[] for _ in range(N+1)]

def dfs():
    answer = []
    # 방문여부 기록을 위한 리스트 노드 갯수만큼 만들기(인덱스 0 이 있으니 하나 더 만들기)
    visitied = [False for _ in range(N+1)]

    # 방문해야할 곳 초기화(처음 시작은 V 이므로 stack 맨 처음에 [V] 넣고 시작)
    to_visits = [V]

    while to_visits:
        # print('dfs ', to_visits, answer)
        current = to_visits.pop()
        # 방문한 적 없다면 - visited[current] 가 False 라면
        if not visitied[current]:
            answer.append(current)
            visitied[current] = True
            # dfs 가 2번부터 깊이탐색 하려고 하려면 거꾸로 넣어줘야함.
            # 그게 아니면 1의 마지막 연결인 4번부터 연결해버림.
            # 사실 dfs 자체에서 순서가 중요한 건 아닌데, 여기선 방문 순서가 중요하므로.
            to_visits += sorted(graph[current], reverse=True)

    return answer


def bfs():
    answer = []

    visited = [False for _ in range(N+1)]

    to_visits = [V]

    while to_visits:
        # print('bfs ', to_visits, answer)
        current = to_visits.pop(0)
        if not visited[current]:
            answer.append(current)
            visited[current] = True
            to_visits += sorted(graph[current])

    return answer


# 시작, 끝 연결 간선
for _ in range(M):
    start, end = map(int, input().split())
    # 단방향
    graph[start].append(end)
    graph[end].append(start)

# print(graph)
print(*dfs())
print(*bfs())

# ??????
