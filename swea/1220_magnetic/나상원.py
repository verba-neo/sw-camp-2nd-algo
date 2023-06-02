import sys
sys.stdin = open('./input.txt')

# T = int(input())
T = 10

for tc in range(1, T+1):
    size = 100
    table = [list(map(int, input().split())) for _ in range(size)]

    print(table)
