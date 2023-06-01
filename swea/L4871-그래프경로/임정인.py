import sys
sys.stdin = open('input.txt')

# vertex 6개, edge 5개 (edge 5개니까 5줄 들어옴)

def dfs():
    # S => G
    # 방문 여부
    visited = [False for _ in range(V+1)]  # 7개, 처음에 있는 건 사용 X
    # 방문할 곳들
    to_visits = [S]  # S로 초기화 하고 시작 / 빈 값이 없을 때까지

    # 앞으로 방문할곳이 남아있다면, 계속 반복 (하나라도 남아있으면 계속 실행)
    while to_visits:
        # 갈 곳 => 방문할 곳들중 마지막(pop)
        current = to_visits.pop()
        # current를 방문한 적이 없으면 가야됨 (있으면 => 가면 안 됨)
        if not visited[current]:
            # 방문하고
            visited[current] = True
            # 추가로 갈 수 있는 곳들을 방문 예정 등록
            to_visits += graph[current]  # 앞으로 갈 곳 추가
    return int(visited[G])


T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())  # 6 5
    # Adj List Graph
    graph = [[] for _ in range(V+1)]


    for _ in range(E):  # E 개의 줄 / 유향그래프
        start, end = map(int, input().split())
        # graph 채우기
        # 단방향
        graph[start].append(end)

        # 양방향 (데이터 수 많아지므로 시간 더 오래걸림)
        # graph[start].append(end)
        # graph[end].append(start)

    S, G = map(int, input().split())

    print(f'#{tc} {dfs()}')
