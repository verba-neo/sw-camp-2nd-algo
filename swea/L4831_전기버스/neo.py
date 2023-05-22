import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())

    # 지금까지의 충전 회수
    charge_count = 0
    stations = [False] * (N+1)

    chargers = list(map(int, input().split()))

    for charge_idx in chargers:
        stations[charge_idx] = True

    # 현재 버스의 위치 idx
    current = K
    # 마지막으로 충전한 정류장 idx
    last_charge = 0

    while current < N:
        # 현재 위치가 충전소라면
        if stations[current]:
            # 1. 충전하고
            charge_count += 1
            # 2. 마지막 충전 위치 갱신
            last_charge = current
            # 3. 최대한 멀리 버스 이동
            current += K

        # 현재 위치가 충전소가 아니라면
        else:
            # 앞 충전소로 이동
            current -= 1

        # 계속 앞으로 오다가, 마지막 충전소에 도착했다면
        if current == last_charge:
            # 실패
            charge_count = 0
            break

    print(f'#{tc} {charge_count}')
