def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n+1)]

<<<<<<< HEAD
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
=======
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
>>>>>>> 18eaa442434aae5d7fc1de0228bbb779e04ff92d

    return answer


# 2
print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
<<<<<<< HEAD
=======

# 1
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
>>>>>>> 18eaa442434aae5d7fc1de0228bbb779e04ff92d
