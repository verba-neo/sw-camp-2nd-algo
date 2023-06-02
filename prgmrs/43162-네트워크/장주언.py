# 독립 된 노드는 하나의 네트워크
# 서로 연결 된 노드들은 하나의 네트워크


def solution(n, computers):
    visited = [False for _ in range(len(computers))]
    answer = 0

    def dfs(computer):
        # 방문표시
        visited[computer] = True

        for idx, com in enumerate(computers[computer]):
            if visited[idx] is False and com != visited[idx]:
                dfs(idx)

    for computer in range(n):
        # 방문을 안했다면
        if visited[computer] is False:
            # dfs 진행
            dfs(computer)
            # dfs가 진행 될 때 +1
            answer += 1

    return answer

# 2
print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))

# 1
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
