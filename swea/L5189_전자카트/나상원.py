import sys
sys.stdin = open('./input.txt')

T = int(input())


# count : 현재 몇개의 구역 방문
# position : 방문 중인 구역
# total : 지금까지 사용한 배터리
def dfs(count, position, total):
    global minimum

    if count == N-1:
        total += battery[position][0]
        minimum = min(minimum, total)

    if total > minimum:
        return

    for idx in range(N):
        if not visited[idx]:
            visited[idx] = True
            dfs(count+1, idx, total+battery[position][idx])
            visited[idx] = False


for tc in range(1, T+1):
    N = int(input())
    battery = [list(map(int, input().split())) for _ in range(N)]

    answer = 100 * N

    visited = [False for _ in range(N)]
    minimum = float('INF')

    visited[0] = True
    dfs(0, 0, 0)
    print(f'#{tc} {minimum}')

