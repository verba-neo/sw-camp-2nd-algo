def solution(n, wires):
    answer = n

    def dfs(now):
        nonlocal count
        visited[now] = True
        count += 1

        for nxt in graph[now]:
            if not visited[nxt]:
                dfs(nxt)

    graph = [[] for _ in range(n+1)]
    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)

    for v1, v2 in wires:
        count = 0
        visited = [False for _ in range(n+1)]
        visited[v2] = True
        dfs(v1)

        diff = abs(count - (n-count))

        if answer > diff:
            answer = diff

    return answer


# 3
print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))

# 0
print(solution(4, [[1,2],[2,3],[3,4]]))

# 1
print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))