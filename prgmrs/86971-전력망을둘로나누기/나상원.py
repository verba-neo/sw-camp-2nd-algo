def solution(n, wires):
    answer = n

    def dfs(s):
        nonlocal count
        visited[s] = True
        count += 1

        for nxt_s in graph[s]:
            if not visited[nxt_s]:
                dfs(nxt_s)

    graph = [[] for _ in range(n+1)]
    for wire1, wire2 in wires:
        graph[wire1].append(wire2)
        graph[wire2].append(wire1)

    for w1, w2 in wires:
        count = 0
        visited = [False for _ in range(n+1)]
        visited[w2] = True
        dfs(w1)

        dif = abs(count - (n-count))

        if answer > dif:
            answer = dif

    return answer


# 3
print(solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))
