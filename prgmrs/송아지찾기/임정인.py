# bfs 너비탐색 이용
# 10001칸 만들어 놓고 사용 (처음 칸은 0으로 두고 시작)
# 이미 한번 사용했던 숫자는 저장하고, 반복해서 사용하지 않도록
# 동일한 숫자를 또 사용해서 무한루프에 빠지지 않도록 주의

# 강사님 답안
def solution(s, e):

    count = 0
    to_visits = [s]  # 목적지
    visited = [False for _ in range(10001)]  # 방문여부

    while to_visits:
        # 현재 목적지 개수만큼 반복
        for _ in range(len(to_visits)):
            # 방문할 목적지
            current = to_visits.pop(0)
            # 방문한 적 없다면
            if not visited[current]:
                # 방문 체크
                visited[current] = True
                # 목적지라면 끝
                if current == e:
                    return count

            # 못 찾았다면 이동 가능한 선택지들
            for nxt in [current-1, current+1, current+5]:
                # 선택지들이 범위 안에 있고, 방문한 적 없다면
                if 0 < nxt <= 10000 and not visited[nxt]:  # and 순서 중요 (범위 먼저 지정 안하면 에러 남)
                    to_visits.append(nxt)

        count += 1

    return count


# (2) 최적화 적용
# double ended queue = deque : 중간자료는 중요하지 않음
from collections import deque  # list pop(0)보다 시간 복잡도 덜함

# e < s : 뒤로 한칸씩 가는 방법밖에 없음
def solution(s, e):
    # 뒤로 갈 때는 최대한 빠르게 가자
    if s > e:
        pass  # count = (e - s) // 5
              # s += count * 5  작은 곳 중에 가장 가까이 보내서 붙여놓고 몇 줄 더 가라고 하자 (적당히 가까운 곳에 붙여주자)
    # 앞으로 가야한다면
    else:
        return s-e
    # count = 0  위에 count 살리면 얘도 같이 살리기
    to_visits = [s]  # 목적지
    visited = [False for _ in range(10001)]  # 방문여부

    while to_visits:
        # 현재 목적지 개수만큼 반복
        for _ in range(len(to_visits)):
            # 방문할 목적지
            current = to_visits.pop(0)  # pop(0) 효율 안 좋아 : 0번째 idx 빠지면 동시에 idx 재정렬 -> 1 idx 는 0으로, 한칸씩 앞당겨짐
            # inqueue 들어오는 것 / dequeue 나가는 것 : 일렬로 안 세우고도 queue 생성 가능
            # 방문한 적 없다면
            if not visited[current]:
                # 방문 체크
                visited[current] = True
                # 목적지라면 끝
                if current == e:
                    return count

            # 못 찾았다면 이동 가능한 선택지들
            for nxt in [current-1, current+1, current+5]:
                # 선택지들이 범위 안에 있고, 방문한 적 없다면
                if 0 < nxt <= 10000 and not visited[nxt]:  # and 순서 중요 (범위 먼저 지정 안하면 에러 남)
                    to_visits.append(nxt)

        count += 1

    return count


# s 	e	result
# 5	    14 	 3
# 8 	3	 5

# 3
print(solution(5, 14))

# 5
print(solution(8, 3))

# 기타 필기
# cycle이 없는 무향 그래프 (자기 자신한테 돌아오지 못함) = 트리
# 싸이클이 생겨버리면 tree 아님
# 상태공간 tree : 송아지 문제
# 루트는 내가 정하기 나름 : 공 달려 있는 실을 내가 들었을 때 기준, 내가 들고 있는게 루트
# 탐색기 검색 bfs

# deque : 양 끝
# heapq : binary, search (max, min) : 가장 큰 값, 가장 작은 값 뺼 때 (최대힙, 최소힙)
# log2(밑)n 시간복잡도
# list ; 탐색 o(n), 추가 o(1), 삭제 o(n) : 지금 있는 거 빼고 재정렬, 가장 최악의 경우 생각
# 정렬 list ; 탐색 o(1), 추가 o(logn), 삭제 o(1)

import heapq
# heapify : heap으로 바꾸다
# l = [3, 4, 8, 7, 4, 2, 9]
# heap.heaplify(l)  # 2, 4, 3, 7, 5, 8, 9
# heapq.heappush(l, 6)  # 2, 4, 3, 6, 5, 8, 9, 7
