# import sys
# sys.stdin = open(('./input.txt'))
#
# T = int(input())
#
# for tc in range(1, T + 1):
#     # N = list(map(int, input().split()))
#     # M = list(map(int, input().split()))
#     N = [10, 3]
#     M = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
#     arr_list = []
#     arr_sum = 0
#     sum_list = []
#
#
#     for add_num in range(N[0]):
#         arr_list.append(M[add_num])
#
#     for sum_cnt in range(N[0]-N[1]+1):
#         for sum_num in arr_list:
#             arr_sum += sum_num
#         sum_list.append(arr_sum)
#
#     print(sum_list)
#
#     print(arr_list)