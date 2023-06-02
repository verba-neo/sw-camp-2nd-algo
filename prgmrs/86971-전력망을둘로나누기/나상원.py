<<<<<<< HEAD
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
=======
def dfs(s, graph, visited):
    count = 1
    visited[s] = True

    for nxt_s in graph[s]:
        if not visited[nxt_s]:
            dfs(nxt_s, graph, visited)

    return count


def solution(n, wires):
    answer = -1
    graph = [[] for _ in range(n+1)]
    visited = [False for _ in range(n+1)]

>>>>>>> 18eaa442434aae5d7fc1de0228bbb779e04ff92d
    for wire1, wire2 in wires:
        graph[wire1].append(wire2)
        graph[wire2].append(wire1)

<<<<<<< HEAD
    for w1, w2 in wires:
        count = 0
        visited = [False for _ in range(n+1)]
        visited[w2] = True
        dfs(w1)

        dif = abs(count - (n-count))

        if answer > dif:
            answer = dif
=======
    dfs(wire1, graph, visited)

    # for wire1, wire2 in wires:
    #     pass
>>>>>>> 18eaa442434aae5d7fc1de0228bbb779e04ff92d

    return answer


# 3
print(solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))
