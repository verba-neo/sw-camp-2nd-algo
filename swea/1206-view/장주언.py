import sys

sys.stdin = open('./input.txt')

T = 10

for tc in range(1, T + 1):
    # 빌딩의 갯수
    N = int(input())
    # 빌딩들의 높이
    buildings = list(map(int, input().split()))
    #조망권 확보 된 세대 수
    count = 0

    #맨 왼쪽 두칸과 오른쪽 두칸은 0
    for idx in range(2, N-2):
        # 비교할 그룹들 중 가장 높은 빌딩
        cg_max = max(buildings[idx-2], buildings[idx-1], buildings[idx+1], buildings[idx+2])
        # 비교했을 때 비교군 중 가장 높은 빌딩보다 높다면
        if buildings[idx] > cg_max:
            # 차이값을  count 에 추가
            count += (buildings[idx] - cg_max)

    print(f'#{tc} {count}')


