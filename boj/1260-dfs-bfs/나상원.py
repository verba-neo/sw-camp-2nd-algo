import sys
sys.stdin = open('input.txt')


def dfs():

    visited = [False for _ in range(N+1)]

    to_visited = [V]
    dfs_result = []

    while to_visited:

        current = to_visited.pop()

        if not visited[current]:
            visited[current] = True
            dfs_result.append(current)
            to_visited += sorted(graph[current], reverse=True)

    return dfs_result


def bfs():

    visited = [False for _ in range(N+1)]

    to_visited = [V]
    bfs_result = []

    while to_visited:

        current = to_visited.pop(0)

        if not visited[current]:
            visited[current] = True
            bfs_result.append(current)
            to_visited += sorted(graph[current])

    return bfs_result


# T = int(input())

# for tc in range(1, T+1):
N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    start, end = map(int, input().split())

    # [양방향]
    graph[start].append(end)
    graph[end].append(start)

print(*dfs())
print(*bfs())
