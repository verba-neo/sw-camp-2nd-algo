# import sys
# sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # print('N', N)

    answer = 0
    for i in range(1, N+1):
        if i % 2 == 1:
            answer += i
        else:
            answer -= i

    print(f'#{tc} {answer}')
