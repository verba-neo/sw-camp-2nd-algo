import sys
sys.stdin = open('input.txt')

T = int(input())

def dfs():
    # S => G

    # 방문 여부
    visitied = [False for _ in range(V+1)]

    # 방문해야할 곳 초기화
    to_visits = [S]

    # 앞으로 방문할 곳이 남아있다면, 계속 반복
    while to_visits:
        # 현재 위치 = 방문할 곳들 중 마지막에 방문한 곳(pop)
        current = to_visits.pop()

        # current 를 방문한 적 없다면
        if not visitied[current]:
            print(current)
            # 이제 방문했으니까 방문 True
            visitied[current] = True

            # 해당 위치에서 추가로 갈 수 있는 곳을 to_visits(방문 예정)에 추가
            to_visits += graph[current]

    return int(visitied[G])



for t in range(1, T+1):
    V, E = map(int, input().split())
    #
    # # 연결 리스트
    # connections = [list(map(int, input().split())) for _ in range(E)]
    # print(connections)
    #
    # # ???

    # Adj List Graph
    graph = [[] for _ in range(V+1)]

    for _ in range(E):
        start, end = map(int, input().split())

        # 단방향 graph 채우기
        graph[start].append(end)

        # # 양방향 graph
        # graph[end].append(start)

    S, G = map(int, input().split())
    print(graph)