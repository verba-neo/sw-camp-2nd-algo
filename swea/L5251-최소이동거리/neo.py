import sys
sys.stdin = open('input.txt')


def dijkstra(s):
    distance[s] = 0

    # 정점 개수만큼 반복
    for _ in range(V+1):
        nxt = -1
        nxt_dist = float('INF')

        # 다음으로 갈 정점을 구해 보자
        for v in range(V+1):
            # 방문 안했고, 더 까가운 곳으로 갱신하자(거리가 더 작은곳이 다음으로 갈 곳)
            if not visited[v] and distance[v] < nxt_dist:
                nxt = v
                nxt_dist = distance[v]

        # 다음 정점 방문
        visited[nxt] = True
        
        # nxt 의 인접 정점들 거리 갱신해 두기
        for nnxt in range(V+1):
            # nxt에서 갈 수 있는곳(간선 존재) and 방문 한적 없음
            if graph[nxt][nnxt] and not visited[nnxt]:
                # 거리 리스트 값을 더 작은 값으로 갱신
                distance[nnxt] = min(distance[nnxt], distance[nxt] + graph[nxt][nnxt])


T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    # 인접 행렬
    graph = [[0 for _ in range(V+1)] for _ in range(V+1)]

    for _ in range(E):
        start, end, weight = map(int, input().split())
        graph[start][end] = weight

    visited = [False] * (V+1)
    distance = [float('INF')] * (V+1)
    dijkstra(0)

    print(f'{tc} {distance[V]}')
