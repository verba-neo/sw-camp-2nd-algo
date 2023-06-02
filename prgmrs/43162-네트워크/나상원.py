def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n+1)]

    def dfs(computer_list, idx, vis):
        # 현재 위치 방문
        visited[idx] = True
        # 다음 방문지 조회,
        for com_idx, linked in enumerate(computers[idx]):
            # 연결 되있으면,
            if linked:
                # 방문을 안했으면,
                if not visited[com_idx]:
                    dfs(computer_list, com_idx, vis)

    for cnt in range(n):
        # dfs 호출 횟수
        if not visited[cnt]:
            dfs(computers, cnt, visited)
            answer += 1

    return answer


# 2
print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))

# 1
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
