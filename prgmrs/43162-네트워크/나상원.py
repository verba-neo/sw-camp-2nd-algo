def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n+1)]

    def dfs(computers, no, visited):
        # 방문 체크
        visited[no] = True
        # idx, 리스트
        for idx, value in enumerate(computers[no]):
            if value == 1:
                if not visited[idx]:
                    dfs(computers, idx, visited)
    # 네트워크 개수 카운트
    for no in range(n):
        if not visited[no]:
            dfs(computers, no, visited)
            answer += 1
        else:
            continue

    return answer


# 2
print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
