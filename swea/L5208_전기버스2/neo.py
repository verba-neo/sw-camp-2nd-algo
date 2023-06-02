for test in range(1, int(input()) + 1):
    N, *battery = map(int, input().split())
    memo = [float('inf')] * N

    memo[N-1] = 0

    for i in range(N-1, -1, -1):
        for j in range(i-1, -1, -1):
            if j + battery[j] >= i:
                memo[j] = min(memo[j], memo[i] + 1)

    print(f'#{test} {memo[0] - 1}')
