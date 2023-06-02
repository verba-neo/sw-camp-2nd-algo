import sys

sys.stdin = open('./input.txt')


def dfs(current, start, total):

    global answer
    # 현재 위치가 끝이라면
    if current == N - 1:
        # answer 값 갱신
        answer = min(answer, total + area[start][0])
        return
    # 범위를 순회하면서
    for i in range(1, N):
        # 방문하지 않았고 i가 start 값이 아닌 경우
        if visited[i] is False and start != i:
            # 방문처리
            visited[i] = True
            # current 값을 올려주고 다음 start에  i 갱신, total 값 갱신
            dfs(current +1, i,  total + area[start][i])
            # 순회하다가 아니면 False처리후 다시 순회
            visited[i] = False


T = int(input())

for tc in range(1, T+1):

    N = int(input())

    area = [list(map(int, input().split())) for _ in range(N)]

    answer = 100 * N

    visited = [False for _ in range(N)]

    dfs(0, 0, 0)

    print(f'#{tc} {answer}')
