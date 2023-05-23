import sys
sys.stdin = open('./input.txt')

T = int(input())

for tc in range(1, T+1):

    N = int(input())
    num = [2, 3, 5, 7, 11]
    answer = [0, 0, 0, 0, 0]

    for j in range(len(num)):
        while True:
            if N % num[j] == 0:
                N = N//num[j]
                answer[j] += 1

            else:
                break
    answer = ' '.join(map(str, answer))

    print(f'#{tc} {answer}')