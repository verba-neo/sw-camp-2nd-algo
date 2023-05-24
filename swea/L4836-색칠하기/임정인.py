import sys
sys.stdin = open('./input.txt')

# 테스트 데이터 개수
T = int(input())

for tc in range(1, T+1):

    N = int(input())
    arr = [[0] * 10 for _ in range(10)]

    for i in range(N):
        color = list(map(int, input().split()))
        for i in range(color[0], color[2]+1):
            for j in range(color[1], color[3]+1):
                arr[i][j] += color[4]

    count = 0
    for i in range(10):
        for j in range(10):
            if arr[i][j] == 3:
                count += 1

    print(f'#{tc} {count}')
