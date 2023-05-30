# N 일 동안의 물건의 매매가를 예측
# 하루에 최대 1만큼 구입
# 판매는 상관없이 가능

import sys

sys.stdin = open('./input.txt')

T = int(input())

for tc in range(1, T+1):
    # N일 간의 가격 예측
    N = int(input())
    # N일 간의 가격 리스트
    price_lst = list(map(int, input().split()))
    # 시세차익 초기화
    benefit = 0
    # 매매가 최대값
    sales = 0

    # 가격 리스트를 반대로 순회
    for price in price_lst[::-1]:
        # 매매가 최대값이 현재 매매가보다 작거나 같으면
        if sales <= price:
            # 현재 매매가를 최대 매매값으로 설정
            sales = price
        # 만약 매매가 최대값이 현재 매매가 보다 클 경우 팔아서 시세 차익을 본다
        else:
            benefit += sales - price

    print(f'#{tc} {benefit}')