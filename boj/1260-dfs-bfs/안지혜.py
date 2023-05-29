# import sys
# sys.stdin = open('input.txt')
#
# N, M, V = map(int, input().split())
# connection_dict = {}
#
# # 관계를 나타내는 딕셔너리 생성
# for _ in range(M):
#     v1, v2 = map(int, input().split())
#
#     if connection_dict.get(v1):
#         connection_dict[v1] = connection_dict[v1] + [v2]
#     else:
#         connection_dict.setdefault(v1, [v2])
#     connection_dict[v1].sort()
#
#     if connection_dict.get(v2):
#         connection_dict[v2] = connection_dict[v2] + [v1]
#     else:
#         connection_dict.setdefault(v2, [v1])
#     connection_dict[v2].sort()
#
#
# def dfs():
#     visited = {}
#     result = []
#     stack = []
#
#     # V를 스택에 push
#     stack.append(V)
#
#     while stack:
#         v = stack.pop()
#
#         if not visited.get(v):
#             visited.setdefault(v, True)
#             result.append(v)
#
#             for i in connection_dict[v][::-1]:
#                 stack += [i]
#
#     return result
#
#
# def bfs():
#     visited = {}
#     result = []
#     queue = []
#
#     queue.append(V)
#
#     while queue:
#         v = queue.pop(0)
#
#         if not visited.get(v):
#             visited.setdefault(v, True)
#             result.append(v)
#
#         for i in connection_dict[v]:
#             if not visited.get(i):
#                 queue.append(i)
#
#     return result


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
            to_visits += sorted(graph[current])
    return history


N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

print(*dfs())
print(*bfs())
