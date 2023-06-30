import sys
sys.stdin = open('input.txt')


# v 정점의 대장 찾아서 return => 결과적으로 족보 root 찾아주는 함수
def find_set(v):
    if v == parents[v]:
        return v
    else:
        """
        # path compression (parents 의 저장 값을 부모 => 대장으로 갱신하기)
        p = find_set(parents[v])
        parents[v] = p
        return p
        """
        return find_set(parents[v])


def union(x, y):
    # x와 y의 대장끼리 합쳐야 함
    # py, px => y의대장, x의대장
    px = find_set(x)
    py = find_set(y)

    """
    # rank 값을 비교하여 Union
    # px, py 중에 랭크가 더 큰 값이 대장
    if ranks[px] > ranks[py]:
        # py의 대장은 px
        parents[py] = px
    elif ranks[px] < ranks[py]:
        # px 의 대장은 py
        parents[px] = py
    # 랭크가 같으면 더 작은 값이 대장
    else:
        py의 대장은 px
        parents[py] = px
        ranks[px] += 1
    """

    # 단순히 작은 값으로 Union
    if px > py:
        # px의 대장은 py
        parents[px] = py
    else:
        # py의 대장은 px
        parents[py] = px


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    graph = []

    for _ in range(E):
        v1, v2, weight = map(int, input().split())

        # Tuple 들로 이루어진 List sort의 기본값 => Tuple의 첫번째 원소 기준이기 때문
        graph.append((weight, v1, v2))

    # Kruskal 의 핵심 => 노드 번호가 아닌, 가중치(weight)로 오름차순 정렬하는 것!
    graph.sort()

    # Make Set                     0  1  2  3  4
    parents = list(range(V+1))  # [0, 1, 2, 3, 4]
    # Rank 다루기
    ranks = [0] * (V+1)

    ans = 0
    for w, v1, v2 in graph:
        # v1 과 v2 가 다른 팀이면,
        if find_set(v1) != find_set(v2):
            # 두 팀을 합친다(선 긋기)
            union(v1, v2)
            # 가중치 를 계속 더한다.
            ans += w

    print(f'#{tc} {ans}')

