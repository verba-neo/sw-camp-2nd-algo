def solution(n, computers):
    graph = [[] for _ in range(n)]

    for idx in range(len(computers)):
        for i, el in enumerate(computers[idx]):
            if i != idx and el == 1:
                graph[idx] += [i]

    visited = [False for _ in range(n)]
    stack = [0]
    net = 0

    while stack:
        current = stack.pop()
        if not visited[current]:
            visited[current] = True
            stack += graph[current]

        if not stack:
            net += 1
            if False in visited:
                i = visited.index(False)
                stack = [i]

    return net


# 2
print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))

# 1
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))