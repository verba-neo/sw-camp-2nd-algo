total = 0
visited = []


def dfs(count, _sum, ability):
    global total
    if count >= len(ability[0]):
        if _sum > total:
            total = _sum
        return

    for i in range(len(ability)):
        if not visited[i]:
            visited[i] = True
            _sum += ability[i][count]
            dfs(count+1, _sum, ability)
            _sum -= ability[i][count]
            visited[i] = False


def solution(ability):
    global total, visited
    visited = [False for i in range(10)]
    dfs(0, 0, ability)

    return total