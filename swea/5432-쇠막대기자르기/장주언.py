# 쇠막대기를 리스트로 받는다

import sys

sys.stdin = open('./input.txt')

T = int(input())

for tc in range(1, T+1):

    iron_rod = input()

    # 막대기의 개수
    rod = 0

    # 조각의 개수
    count = 0

    # 인덱스
    idx = 0

    while True:
        if idx + 1 > len(iron_rod):
            break

        elif iron_rod[idx] == '(':
            rod += 1
        elif iron_rod[idx] == ')':
            if iron_rod[idx-1] == '(':
                rod -= 1
                count += rod
            else:
                rod -= 1
                count += 1

        idx += 1

    print(f'#{tc} {count}')