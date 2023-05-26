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
