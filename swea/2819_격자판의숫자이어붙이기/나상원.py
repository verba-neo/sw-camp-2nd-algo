import sys
sys.stdin = open('./input.txt')

T = int(input())

for tc in range(1, T+1):
    board = [list(map(int, input().split())) for _ in range(4)]

    answer = 0

    print(f'#{tc} {answer}')
