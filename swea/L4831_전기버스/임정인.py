# N : 0~N 번까지 이동
# K : 한 번 충전으로 최대한 이동할 수 있는 정류장 수
# M : 충전기 설치된 정류장 번호

# K 만큼 거리 던져보기 : 충전소 있으면 거기서 충전
# 없으면 : 그 전에 위치한 정류장에서 충전

import sys
sys.stdin = open('./input.txt')

# 테스트 데이터 개수
T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())

    # 지금까지 충전횟수
    charge_count = 0

    # 충전기 설치된 정류장
    stations = [False] * (N+1)
    chargers = list(map(int, input().split()))

    for charge_idx in chargers:
        stations[charge_idx] = True

    # 디버깅 : 중간중간 프린트 하면서 맞는 방향으로 가고 있는지 확인

    # 현재 버스의 위치 idx
    current = K  # 최대한 멀리 보내놓고 시작
    # 마지막으로 충전한 정류장 idx
    last_charge = 0  # 0은 차고지

    while current < N:  # N = 종점의 idx
        # 현재 위치가 충전소라면 1, 충전하고 2, 마지막 충전위치 갱신
        if stations[current]:  # current = True 라면
            # 1. 충전하고
            charge_count += 1
            # 2. 마지막 충전 위치 갱신
            last_charge = current
            # 3. 최대한 멀리 버스 이동
            current += K

        # 현재 위치가 충전소가 아니라면
        else:
            # 앞 충전소로 이동
            current -= 1  # 충전소 없으니까 거꾸로 한 칸씩 오면서 충전소 찾기

        # 계속 앞으로 오다가, 마지막 충전소에 도착했다면
        if current == last_charge:  # 내 위치가 마지막 충전 장소라면
            # 실패
            charge_count = 0
            break

    print(f'#{tc} {charge_count}')
