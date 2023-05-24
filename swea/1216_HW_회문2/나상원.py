import sys
sys.stdin = open('./input.txt')

# T = int(input())
T = 10

for tc in range(1, T+1):
    t = input()
    N = 100
    char_list = [list(map(str, input())) for _ in range(N)]

    # for row_idx in range(100):

