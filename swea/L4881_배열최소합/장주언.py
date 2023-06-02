import sys

sys.stdin = open('./input.txt')


def dfs(idx, _sum):
    global answer
    # _sum 값이 answer보다 커지면 그만
    if _sum > answer:
        return
    # idx가 N과 같을 때 answer와 _sum 비교
    if idx == N:

        if answer > _sum:
            answer = _sum
            return
    # i를 돌아가면서 모두 탐색. 같은 idx 안에서 돌게 되니까 visited에 있는 i에는 들어가지 않는다
    for i in range(N):
        if i not in visited:
            visited.append(i)
            dfs(idx+1, _sum+lst[idx][i])
            visited.pop()


T = int(input())

for tc in range(1, T+1):

    N = int(input())

    lst = [list(map(int, list(input().split()))) for _ in range(N)]

    visited = []

    answer = 10 * N

    dfs(0, 0)

    print(f'#{tc} {answer}')

