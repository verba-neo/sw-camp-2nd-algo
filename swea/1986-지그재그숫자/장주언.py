import sys

sys.stdin = open('./input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    answer = 1

    for i in range(2, N + 1):
        if i % 2 == True:
            answer += i
        else:
            answer -= i

    print(f'#{tc} {answer}')