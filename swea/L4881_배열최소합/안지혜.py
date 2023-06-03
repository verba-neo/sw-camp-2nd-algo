import sys
from itertools import permutations
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr_list = [list(map(int, input().split())) for _ in range(N)]
    answer = float('INF')

    visited = [False] * N


    def dfs(row, total):
        global answer

        if row == N:
            if answer > total:
                answer = total

        for col in range(N):
            if not visited[col]:
                visited[col] = True
                dfs(row+1, total+arr_list[row][col])
                visited[col] = False

    dfs(0, 0)

    print(f'#{tc} {answer}')
