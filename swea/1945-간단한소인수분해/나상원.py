import sys
sys.stdin = open('./input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    num = [2, 3, 5, 7, 11]
    count = [0, 0, 0, 0, 0]

    for i in range(len(num)):
        while True:
            if N % num[i] == 0:
                N = N//num[i]
                count[i] += 1
            else:
                break

    num_count = ' '.join(map(str, count))

    print(f'#{tc} {num_count}')