import sys
from itertools import permutations
sys.stdin = open('input.txt')

# 기존코드
# T = int(input())
#
# for tc in range(1, T + 1):
#     N = int(input())
#     arr_list = [list(map(int, input().split())) for _ in range(N)]
#     answer = float('INF')
#
#     stack = [(0, 0)]
#     visited = [False for _ in range(N)]
#
#
#     def dfs(lv, total):
#         global answer, stack
#
#         while stack:
#             cur_i, cur_num = stack.pop()
#             total += cur_num
#
#             if answer < total:
#                 return
#
#             if lv < N:
#                 next_arr = arr_list[lv]
#
#                 for i, el in enumerate(next_arr):
#                     if not visited[i]:
#                         visited[i] = True
#                         stack += [(i, el)]
#                         dfs(lv + 1, total)
#                         visited[i] = False
#
#             elif lv == N:
#                 if answer > total:
#                     answer = total
#
#
#     dfs(0, 0)
#
#     print(f'#{tc} {answer}')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr_list = [list(map(int, input().split())) for _ in range(N)]
    answer = float('INF')

    visited = [False] * N


    def dfs(row, total):
        global answer

        if row == N:
            if answer > total:
                answer = total

        # Pruning => Backtracking
        if answer < total:
            return

        for col in range(N):
            if not visited[col]:
                visited[col] = True
                dfs(row+1, total+arr_list[row][col])
                visited[col] = False

    dfs(0, 0)

    print(f'#{tc} {answer}')
