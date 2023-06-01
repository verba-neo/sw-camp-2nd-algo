# 하나를 끊고 방문했다고 표시
# 전력망 그래프 만들기
# 탐색 시작. 노드 개수 구하기 => 1번째 전력망 개수
# 2번째 전력망 개수는 전체 전력망에서 1번째 전령망 뺀거
# 두 전력망 개수의 차로 절댓값 가장 작은 것 => 답


def solution(n, wires):
    answer = n

    for idx, wire in enumerate(wires):
        visited = [False for _ in range(n + 1)]
        visited[wire[0]] = True
        v = wire[1]

        sliced_wires = wires[:idx] + wires[idx+1:]

        graph = [[] for _ in range(n + 1)]
        for i in range(len(sliced_wires)):
            start, end = sliced_wires[i]
            graph[start].append(end)
            graph[end].append(start)

        to_visits = [v]
        web_1_node = 0
        while to_visits:
            current = to_visits.pop()
            if not visited[current]:
                visited[current] = True
                web_1_node += 1
                to_visits += graph[current]

        web_2_node = n - web_1_node
        node_abe = abs(web_2_node - web_1_node)

        answer = node_abe if node_abe < answer else answer


    return answer

# 3
print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))

# 0
print(solution(4, [[1,2],[2,3],[3,4]]))

# 1
print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))