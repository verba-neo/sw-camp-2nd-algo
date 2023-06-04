import sys
sys.stdin = open('input.txt')



def sol_perm(n):
    from itertools import permutations
    minimum = float('INF')
    for case in permutations(range(n)):
        total = 0
        for idx in range(n):
            total += matrix[idx][case[idx]]

    if minimum > total:
        minimum = total

    return minimum


def dfs(row, total):
    global answer
    if row == N:
        answer = total if total < answer else answer
        return

    # 가지치기(Pruning) => Backtracking
    if answer < total:
        return

    for col in range(N):
        if not col_visited[col]:
            col_visited[col] = True
            dfs(row+1, total+matrix[row][col])
            col_visited[col] = False


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    answer = float('INF')
    col_visited = [False] * N
    dfs(0, 0)
    # print(sol_perm(N))
    print(f'#{tc} {answer}')
