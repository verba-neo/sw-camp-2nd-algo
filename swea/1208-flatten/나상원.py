import sys
sys.stdin = open('./input.txt')

# T = int(input())
T = 10

for tc in range(1, T + 1):
    answer = 0

    N = int(input())
    H = list(map(int, input().split()))

    for dump in range(N):
        max_idx = H.index(max(H))
        min_idx = H.index(min(H))

        H[max_idx] -= 1
        H[min_idx] += 1

    answer = max(H) - min(H)

    print(f'#{tc} {answer}')
