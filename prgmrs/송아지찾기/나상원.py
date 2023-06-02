def solution(s, e):
    answer = 0

    visited = [False for _ in range(10001)]
    jump = [-1, 1, 5]
    to_vis = [s]
    cnt = 0

    while to_vis:
        # 현재 목적지 개수 만큼 반복
        for _ in range(len(to_vis)):
            # 방문할 목적지 갱신
            # pop(0)의 효율성이 생각되면 deque() 사용해보자.
            current = to_vis.pop(0)
            # 방문한 적이 없다면,
            if not visited[current]:
                # 방문 체크
                visited[current] = True
                # 못 찾았다면 이동가능한 선택지
                for jp in jump:
                    # 선택지들이 범위 안에 있고, 방문한 적 없다면,
                    # if 0 < current+jp <= 10000 and not visited[current+jp]:
                    to_vis.append(current+jp)

        if visited[e]:
            return cnt

        cnt += 1
    answer += cnt

    return answer


print(solution(5, 14))
print(solution(8, 3))
# print(solution(7845, 16))
