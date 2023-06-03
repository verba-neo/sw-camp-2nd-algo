from collections import deque


def solution(n, computers):
    answer = 0

    isvisit = [0] * n

    # dfs
    # dfs로 노드번호가 들어오면
    def dfs(idx):
        # 해당 노드를 방문처리(1)하고
        isvisit[idx] = 1
        # bfs 의 computer 확인처럼 해당 컴퓨터(idx)의 모든 연결상태를 확인하면서 dfs 로 보냄.
        # q에 넣기. dfs에 넣기만 다르고 같다.
        for side in range(n):
            if isvisit[side] == 0 and computers[idx][side]:
                dfs(side)
            print(isvisit)

    # bfs
    # bfs 에 처음 들어온 시작점 idx 를 q에 넣고,
    def bfs(idx):
        q = deque()
        q.append(idx)
        while q:
            i = q.popleft()
            # q 에 있는 걸 하나씩 빼면서 방문처리함.
            # 그럼 q에 어떤 걸 넣느냐가 중요함.
            isvisit[i] = 1
            # 각 computer는 전체 node 수 만큼의 길이를 가진 list 를 가지고 연결 상태를 가지고 있으므로,
            # range(n)으로 q에서 빼낸 현재 computer 의 index 전체를 돌아가면서: computer[i] 의 [a]
            # 0이 아니거나(연결되어있거나) 방문한적 없다면 -> q 에 넣어서 q에서 빼내질 때 방문처리합니다.
            # 연결이 끝나면 q에 넣을 게 없으므로(0)
            for a in range(n):
                if computers[i][a] != 0 and isvisit[a] == 0:
                    q.append(a)

    for nodeidx in range(n):
        # node 를 돌면서 방문 안 한 친구들을 방문한 뒤에 answer 를 +1
        # 왜 바로 +1 을 합니까? 첫번째 node를 돌아도 isvisit가 (0)이면
        # 끊어져있는 것이므로, 새롭게 방문(dfs, bfs)하면서 answer +1
        if isvisit[nodeidx] == 0:
            # dfs(nodeidx)
            bfs(nodeidx)
            answer += 1

    print(answer)
    return answer


# 2
print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))

# 1
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
