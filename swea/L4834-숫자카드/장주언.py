# 숫자카드를뽑는다.
# 숫자에는 0에서 9까지 숫자가 적혀있다.
# 가장 카드가 많은 숫자와, 그 카드의 수를 출력하라
# 만약 카드의 수가 같다면 높은 숫자의 카드가 나온다.

import sys

sys.stdin = open('./input.txt')

T = int(input())

for tc in range(1, T + 1):

    # N개의 카드 장수
    N = int(input())

    # N개의 숫자
    ai = list(map(int, input()))

    # 0에서 9까지의 카드 장수를 세어 줄  count_lst 초기화 및 생성
    count_lst = [0] * 10
    # ai를 순회하면서 숫자를 카운팅한다.
    for num in ai:
        count_lst[num] += 1
    # count_lst에서 가장 큰 장수와 해당 idx를 뽑아낸다.
    max_count = 0
    max_idx = 0
    for idx in range(len(count_lst)):
        if count_lst[idx] >= max_count:
            max_count = count_lst[idx]

            if idx > max_idx:
                max_idx = idx


    print(f'#{tc} {max_idx} {max_count}')









