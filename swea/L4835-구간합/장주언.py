# N개의 정수가 들어간 배열
# M개의 합
# 가장 큰 합과 가장 작은 합의 차이

import sys

sys.stdin = open('./input.txt')

T = int(input())



for tc in range(1, T + 1):
    # N개의 정수, M개의 합
    N, M = map(int, input().split())

    # N개의 정수가 들어간 리스트 생성
    ai = list(map(int, input().split()))

    max = 0
    min = 10000 * N

    for idx in range(0, N + 1 - M):
        # 구간 나누기
        section = ai[idx:idx + M]


        if sum(section) >= max:
            max = sum(section)

        if sum(section) < min:
            min = sum(section)


    result = max - min

    print(f'#{tc} {result}')
