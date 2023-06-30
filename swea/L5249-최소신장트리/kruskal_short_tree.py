import sys
sys.stdin = open('input.txt')


def find_set(v):
    return v if v == parents[v] else find_set(parents[v])


def union(x, y):
    x, y = find_set(x), find_set(y)
    if x > y:
        x, y = y, x
    parents[y] = x


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    graph = []

    for _ in range(E):
        v1, v2, weight = map(int, input().split())
        graph.append((weight, v1, v2))
    graph.sort()

    parents = list(range(V+1))
    ans = 0
    # 트리 저장할 리스트
    mst = []

    for w, v1, v2 in graph:
        if find_set(v1) != find_set(v2):
            union(v1, v2)
            ans += w
            # 트리의 간선정보 입력
            mst.append((v1, v2))

    print(mst)
    print(f'#{tc} {ans}')

