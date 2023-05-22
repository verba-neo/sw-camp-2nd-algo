import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    divs = [2, 3, 5, 7, 11]
    answer = []

    for div in divs:
        cnt = 0
        while N % div == 0:
            N //= div
            cnt += 1
        answer.append(cnt)

    answer = ' '.join(map(str, answer))
    print(f'#{tc} {answer}')
