import sys

sys.stidin = open('./input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    print(tc, N)
