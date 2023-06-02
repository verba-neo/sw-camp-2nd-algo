import sys
sys.stdin = open('input.txt')


def dfs(count, zone, total):
    """
    count: 현재 몇 개의 구역을 방문 했는지
    zone: 지금 방문 중인 구역 번호
    total: 지금까지 사용한 배터리 총량
    """
    global minimum
    if count == N-1:
        total += matrix[zone][0]
        minimum = min(minimum, total)

    if total > minimum:
        return

    for nxt in range(N):
        if not zone_check[nxt]:
            zone_check[nxt] = True
            dfs(count+1, nxt, total+matrix[zone][nxt])
            zone_check[nxt] = False


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    zone_check = [False] * N
    minimum = float('inf')

    zone_check[0] = True
    dfs(0, 0, 0)
    print(f'#{tc} {minimum}')
