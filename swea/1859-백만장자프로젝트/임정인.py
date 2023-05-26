import sys
sys.stdin = open('./input.txt')

# 테스트 데이터 개수
T = int(input())  # 3

# 연속 N일 동안 물건 매매가 예측해서 알고 있음
# 하루 최대 1만큼 구입 가능
# 판매는 원할 때 가능

# ex) -3 -5 +18 / -3 +5 0
# -1 -1 +6 -1 +2 = 5

for tc in range(1, T+1):

    N = int(input())  # 3 / 3 / 5
    value = list(map(int, input().split()))  # 매매가
    profit = 0
    max_price = value[-1]  # 마지막 값을 최대값으로 설정

    for i in range(N-2, -1, -1):  # 끝에서 두 번재 값부터 -1씩 감소하면서 0까지
        if value[i] >= max_price:  # 이전 값 >= 다음 값 : 구매X
            max_price = value[i]  # => profit 변동 X, 최대값만 변경
        else:
            profit += max_price - value[i]  # 이전 값 < 다음 값 : 구매O
            # max_price 에서 현재 값의 차이가 최대값이므로 profit 이 될 수 있음

    print(f'#{tc} {profit}')

# (2) 강사님 풀이

for tc in range(1, T+1):
    N = int(input())
    prices = list(map(int, input().split()))
    # 총 benefit / 최대 가격
    total = max_price = 0

    # 미래를 보는 능력이 있으니까 미래부터 풀어오기
    # for price in prices[::-1]:  # 시간 복잡도 0(n)

    # 가장 먼 미래부터 지금까지 가격 확인
    for idx in range(N-1, -1, -1):
        price = prices[idx]

        if price > max_price:
            # 팔아야 하는 가격
            max_price = price
        # 지금 가격이 더 싸다면,
        else:
            # 바로 이윤 계산
            profit = max_price - price
            total += profit



    print(f'#{tc} {total}')

