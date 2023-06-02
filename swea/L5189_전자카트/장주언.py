import sys

sys.stdin = open('./input.txt')


def dfs(current, start, total):
    global answer

    if current == N - 1:
        answer = min(answer, total + area[start][0])
        return

    for i in range(1, N):
        if visited[i] is False and start != i:
            visited[i] = True
            dfs(current +1, i,  total + area[start][i])
            visited[i] = False


T = int(input())

for tc in range(1, T+1):

    N = int(input())

    area = [list(map(int, input().split())) for _ in range(N)]

    answer = 100 * N

    visited = [False for _ in range(N)]

    dfs(0, 0, 0)

    print(f'#{tc} {answer}')
