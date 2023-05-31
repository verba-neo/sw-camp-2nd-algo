from collections import deque


def solution(s, e):
    # 뒤로 갈때는 최대한 빠르게 가자.
    if s < e:
        count = (e - s) // 5
        s += count * 5
    # 앞으로 가야 한다면
    else:
        return s - e

    to_visits = deque()
    to_visits.append(s)

    visited = [False for _ in range(10001)]

    while to_visits:
        # 현재 목적지 개수만큼 반복
        for _ in range(len(to_visits)):
            # 방문할 목적지
            current = to_visits.popleft()
            # 방문한 적 없다면
            if not visited[current]:
                # 방문 체크
                visited[current] = True

                # 목적지라면 끝
                if current == e:
                    return count

                # 못 찾았다면 이동 가능한 선택지들
                for nxt in [current-1, current+1, current+5]:
                    # 선택지들이 범위 안에 있고, 방문한적 없다면,
                    if 0 < nxt <= 10000 and not visited[nxt]:
                        to_visits.append(nxt)

        count += 1


# 3
print(solution(5, 14))

# 5
print(solution(8, 3))


'''
테스트 1 〉	통과 (2.07ms, 10.3MB)
테스트 2 〉	통과 (0.43ms, 10.2MB)
테스트 3 〉	통과 (7.24ms, 10.3MB)
테스트 4 〉	통과 (7.94ms, 10.3MB)
테스트 5 〉	통과 (0.34ms, 10.2MB)
테스트 6 〉	통과 (5.44ms, 10.4MB)
테스트 7 〉	통과 (7.07ms, 10.2MB)
테스트 8 〉	통과 (0.48ms, 10.3MB)
테스트 9 〉	통과 (12.88ms, 10.3MB)
테스트 10 〉	통과 (0.34ms, 10.3MB)

테스트 1 〉	통과 (0.32ms, 10.3MB)
테스트 2 〉	통과 (0.00ms, 10.1MB)
테스트 3 〉	통과 (0.00ms, 10.1MB)
테스트 4 〉	통과 (0.34ms, 10.4MB)
테스트 5 〉	통과 (0.62ms, 10.2MB)
테스트 6 〉	통과 (0.30ms, 10.4MB)
테스트 7 〉	통과 (0.34ms, 10.2MB)
테스트 8 〉	통과 (0.00ms, 10.1MB)
테스트 9 〉	통과 (0.38ms, 10.4MB)
테스트 10 〉	통과 (0.34ms, 10.3MB)

테스트 1 〉	통과 (0.33ms, 10.3MB)
테스트 2 〉	통과 (0.00ms, 10.2MB)
테스트 3 〉	통과 (0.00ms, 10.2MB)
테스트 4 〉	통과 (0.58ms, 10.3MB)
테스트 5 〉	통과 (0.33ms, 10.4MB)
테스트 6 〉	통과 (0.33ms, 10.2MB)
테스트 7 〉	통과 (0.55ms, 10.3MB)
테스트 8 〉	통과 (0.00ms, 10.4MB)
테스트 9 〉	통과 (0.31ms, 10.2MB)
테스트 10 〉	통과 (0.34ms, 10.3MB)
'''