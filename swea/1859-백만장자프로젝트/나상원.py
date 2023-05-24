# import sys
# sys.stdin = open('./input.txt')
#
# T = int(input())
#
# for tc in range(1, T+1):
#     N = int(input())
#     M = list(map(int, input().split()))
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
