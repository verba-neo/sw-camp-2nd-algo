# import sys
# sys.stdin = open('./start.txt')
#
# T = int(start())
#
# for tc in range(1, T+1):
#     N = int(start())
#     M = list(map(int, start().split()))
#
#     benefit = 0
#     sale_idx = 0
#
#     if M[0] == max(M):
#         pass
#     else:
#         for days in range(N):
#             if M[days] <= max(M):
#                 benefit += max(M) - M[days]
#     print(benefit)
#

import sys
sys.stdin = open('./input.txt')

T = int(input())

for tc in range(1, T+1):
    days = int(input())
    prices = list(map(int, input().split()))

    # 마진
    benefit = 0

    # 최대 가격
    max_pri = 0
    
    # 뒤에서 부터 최대 가격 비교 하면서 작으면 차이 만큼 마진에 더함, 더 큰 값이 나오면 최대값 갱신
    # 복잡도 O(n)
    # for pri in prices(N-1, -1, -1)
    for pri in prices[::-1]:
        # 지금 가격이 더 비싸다면,
        if pri > max_pri:
            # 팔아야 하는 가격
            max_pri = pri
        # 지금 가격이 더 싸다면,
        else:
            # 마진 계산
            benefit += max_pri - pri

    print(f'#{tc} {benefit}')
