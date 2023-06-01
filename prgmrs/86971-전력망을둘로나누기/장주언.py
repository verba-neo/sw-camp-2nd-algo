# # n개의 송전탑, 각 송전탑을 잇는 전선 정보 wires
# # 하나의 wire를 끊어내서 전력망을 두개로 나눈다.
# # 두 전력망의 송전탑 개수가 비슷하도록 끊어내고 싶다.
# # 두 전력망의 송전탑 개수를 return하라
# # 2 <= n <= 100
# # len(wires) = n-1
# # wires = [[v1, v2]]
# # 1 <= v1 < v2 <= n

from collections import deque


def solution(n, wires):
    answer = n
    # 그래프 초기화
    graph = [[] for _ in range(n+1)]
    # wires가 v1 < v2 인 특징을 이용 graph를 채워 넣는다.
    for start, end in wires:
        graph[start].append(end)
        graph[end].append(start)
    # print(graph)

    for v1, v2 in wires:
        visited = [False for _ in range(n + 1)]

        to_visit = deque()
        to_visit.append(v1)
        # 각 송전탑의 개수를 세어야 하므로 첫 송전탑 +1로 시작한다.
        result = 1

        # 미리 끊어놓을 전력망들을 True로 설정
        visited[v1] = True
        visited[v2] = True

        while to_visit:
            # 현재 위치를 to_visit에서 popleft로 가져오고
            current = to_visit.popleft()
            # graph[current]의 송전탑 넘버들을 확인한다.
            for v in graph[current]:
                # 송전탑을 방문하지 않았으면
                if not visited[v]:
                    # 송전탑 개수를 더해준다.
                    result += 1

                    # 방문후 True로 바꿔주고
                    visited[v] = True

                    # to_visit에 추가
                    to_visit.append(v)

        few = min(result, n-result)
        many = max(result, n-result)

        if answer > many - few:

            answer = many - few

    return answer


# 3
print(solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))

# 0
print(solution(4, [[1, 2], [2, 3], [3, 4]]))

# 1
print(solution(7, [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]))
