import sys
sys.stdin = open('./input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    answer = 0
    for j in range(1, N+1):
        if j % 2 == 0:
            answer = answer - j
        else:
            answer = answer + j

    print(f'#{tc} {answer}')
