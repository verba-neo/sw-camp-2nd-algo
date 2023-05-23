# 0에서 출발해 종점인 N번 정류장
# 한번 충전하면 최대한 이동할 수 있는 정류장 수 K
# 충전기가 설치된 M개의 정류장 번호
# 최소 충전 횟수 => '최소'가 포인트
# 충전기 설치가 잘못된 경우 0을 출력한다. 출발지의 충전기는 충전횟수에 포함 x

import sys

sys.stdin = open('./input.txt')

T = int(input())

for tc in range(1, T + 1):

    K, N, M = list(map(int, input().split()))

    charge_list = list(map(int, input().split()))

    count = 0

    bus_now = 0

    # 현재 버스 위치에서 최대거리를 이동할 경우가 < N보다 작을 때 까지
    while bus_now + K < N:
        # 최소충전횟수를 뽑아야 하므로 K만큼 가서 확인
        for move in range(K, 0, -1):
            #이동한 칸수에 충전소가 있는지 확인
            if (bus_now + move) in charge_list:
                # 이동한 칸수만큼 버스를 위치를 갱신해주고
                bus_now += move
                # 충전횟수 증가
                count += 1

                break
        # 충전소가 없으면 0
        else:
            count = 0

            break

    print(f'#{tc} {count}')

