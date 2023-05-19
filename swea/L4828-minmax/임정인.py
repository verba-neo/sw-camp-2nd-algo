import sys
sys.stdin = open('./input.txt')

T = int(input())

for tc in range(1, T+1):
    input()
    i = list(map(int, input().split(" ")))
    answer = max(i) - min(i)

    print(f'#{tc} {answer}')