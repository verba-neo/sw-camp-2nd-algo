# N개의 양의 정수
# 5 <= N <= 1000
# N개의 양수 ai

import sys

sys.stdin = open('./input.txt')

T = int(input())

for tc in range(1, T+1):

    N = int(input())
    ai = list(map(int, input().split()))

    max_num = ai[0]
    min_num = ai[0]

    for num in ai:
        if max_num <= num:
            max_num = num

        if min_num >= num:
            min_num = num

    answer = max_num - min_num

    print(f'#{tc} {answer}')




