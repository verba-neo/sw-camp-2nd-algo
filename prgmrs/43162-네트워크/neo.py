def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]

    def dfs(v):
        visited[v] = True
        for nxt in range(n):
            if not visited[nxt] and computers[v][nxt]:
                dfs(nxt)

    for v in range(n):
        if not visited[v]:
            dfs(v)
            answer += 1

    return answer

