import sys
sys.stdin = open(('./input.txt'))

T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    station_charger = list(map(int, input().split()))

    station = [0] * (N+1)
    # stations = [False] * (N+1)

    for cn in station_charger:
        station[cn] += 1
    
    # 충전 횟수
    charge_count = 0

    # 현재 위치
    now_loc = 0

    while now_loc < N:

        if station[now_loc + K]:
            now_loc = now_loc + K
            charge_count += 1
        else:
            for back in range(1, K):
                if station[now_loc+K-back]:
                    now_loc = now_loc + K - back
                    charge_count += 1
                    break
            else:
                charge_count = 0
                break

        if now_loc + K >= N:
            now_loc = N

    # # 충전 횟수
    # charge_cnt = 0
    #
    # for charge_idx in station_charger:
    #     stations[charge_idx] = True
    #
    # # 현재 버스의 위치 idx
    # current = K
    # # 마지막으로 충전한 위치 idx
    # last_charge = 0
    #
    # while current < N:
    #     # 현재 위치가 충전소라면, 1. 충전하고 2. 마지막 충전 위치 갱신
    #     if stations[current]:
    #         # 1. 충전
    #         charge_cnt += 1
    #         # 2. 마지막 충전 위치 갱신
    #         last_charge = current
    #         # 3. 최대한 멀리 버스 이동
    #         current += K
    #
    #     # 현재 위치가 충전소가 아니라면
    #     else:
    #         # 앞 충전소로 이동
    #         current -= 1
    #     # 계속 앞으로 오다가, 마지막 충전소에 도착했다면
    #     if current == last_charge:
    #         # 실패 노선
    #         charge_cnt = 0
    #         break
    #
    # # print(f'#{tc} {charge_count}')
    print(f'#{tc} {charge_count}')
