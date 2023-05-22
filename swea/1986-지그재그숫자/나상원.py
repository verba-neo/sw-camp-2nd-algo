import sys
sys.stdin = open('./input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    answer = 0

    for num in range(N+1):
        if num % 2 != 0:
            answer += num
        else:
            answer -= num
    print(f'#{tc} {answer}')