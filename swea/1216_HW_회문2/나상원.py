import sys
sys.stdin = open('./input.txt')

# T = int(input())
T = 10

for tc in range(1, T+1):
    t = input()
    N = 100
    char_list = [list(map(str, input())) for _ in range(N)]

    char_idx = 0
    forward_char = []
    reverse_char = []

    # for row_idx in range(N):
    #
    #     for col_idx in range(N):
    #         if char_list[row_idx][col_idx] == char_list[row_idx][N-1]: