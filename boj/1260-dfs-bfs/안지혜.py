# import sys
# sys.stdin = open('input.txt')

N, M, V = map(int, input().split())
connection_dict = {}

# 관계를 나타내는 딕셔너리 생성
for _ in range(M):
    v1, v2 = map(int, input().split())

    if connection_dict.get(v1):
        connection_dict[v1] = connection_dict[v1] + [v2]
        connection_dict[v1].sort()
    else:
        connection_dict.setdefault(v1, [v2])
        connection_dict[v1].sort()

    if connection_dict.get(v2):
        connection_dict[v2] = connection_dict[v2] + [v1]
        connection_dict[v2].sort()
    else:
        connection_dict.setdefault(v2, [v1])
        connection_dict[v2].sort()

# 인접 접점 중, 방문 안 한 w 값 찾는 함수
def search_w_unvisited(v, visited):
    w = None
    for el in connection_dict[v]:
        if visited.get(el) != True:
            w = el
            break
    return w


def dfs():
    visited = {}
    result = []
    stack = []

    # visited 에 1번째 v 를 True로 바꾸기, v를 스택에 push
    result.append(V)
    visited.setdefault(V, True)
    stack.append(V)
    v = V

    while v:
        # 방문 안 한 w 찾기
        w = search_w_unvisited(v, visited)

        # w 방문, w push, w를 v 로 바꿈.
        while w:
            result.append(w)
            visited.setdefault(w, True)
            stack.append(w)
            v = w
            w = search_w_unvisited(v, visited)

        if stack:
            v = stack.pop()
        else:
            break

    return result


def bfs():
    pass


dfs_result = dfs()

print(dfs_result)