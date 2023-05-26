import sys
sys.stdin = open('./input.txt')


def dfs():
    # S => G
    # 방문 여부
    visited = [False for _ in range(V+1)]
    # 방문할 곳들
    to_visits = [S]
    # 앞으로 방문할 곳이 남아있다면, 계속 반복
    while to_visits:
        # 현재 위치 => 방문할 곳들중 마지막 (pop)
        current = to_visits.pop()
        # current를 방문한 적이 없으면
        if not visited[current]:
            # print(current, end ='')
            # 방문하고
            visited[current] = True
            # 추가로 갈 수 있는 곳들을 방문 예정 등록
            to_visits += graph[current]

    return int(visited[G])

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    # Adj List Graph
    graph = [[] for _ in range(V+1)]

    for _ in range(E):
        start, end = map(int, input().split())
        # graph 채우기
        # 단방향
        graph[start].append(end)

        # 양방향
        # graph[start].append(end)
        # graph[end].append(start)

    S, G = map(int, input().split())

    print(f'#{tc} {dfs()} ')