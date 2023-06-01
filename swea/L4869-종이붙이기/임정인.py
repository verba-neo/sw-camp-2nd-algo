# stack 없이 자유롭게 풀기 / 회귀 가능

import sys
sys.stdin = open('input.txt')

# 테스트 데이터 개수
T = int(input())  # 3

def make_square(n):
    if n == 1:
        return 1
    if n == 2:
        return 3

    return make_square(n-1) + 2 * make_square(n-2)


for tc in range(1, T+1):
    width = int(input()) // 10
    print(f'#{tc} {make_square(width)}')

