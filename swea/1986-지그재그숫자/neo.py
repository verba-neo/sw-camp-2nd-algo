import sys
sys.stdin = open('./input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    answer = 0

    for i in range(1, N+1):
        answer = answer + i if i % 2 else answer - i

    print(f'#{tc} {answer}')
