# 쇠막대기를 리스트로 받는다

import sys

sys.stdin = open('./input.txt')

T = int(input())

for tc in range(1, T+1):

    iron_rod = list(map(str, input()))

    # 막대기의 개수
    rod = 0

    # 조각의 개수
    count = 0

    # 인덱스
    idx = 0

    while True:
        # iron_rod의 범위를 넘어가면 break
        if idx + 1 > len(iron_rod):
            break
        # '(' 일 때 막대기의 갯수 추가
        elif iron_rod[idx] == '(':
            rod += 1
        # ')' 일 때
        elif iron_rod[idx] == ')':
            # 바로 직전에 '(' 여서 레이져였다면
            if iron_rod[idx-1] == '(':
                # 막대기의 갯수를 하나 빼주고
                rod -= 1
                # 조각의 갯수에 막대기 갯수만큼 추가
                count += rod
            # 레이저가 아닌 ')'였다면, 막대의 갯수를 빼주고 조각을 하나 추가해준다.
            else:
                rod -= 1
                count += 1

        idx += 1

    print(f'#{tc} {count}')