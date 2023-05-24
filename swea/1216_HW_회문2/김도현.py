from itertools import combinations_with_replacement

import sys
sys.stdin = open('input.txt')

for t in range(1, 11):
    t = input()
    # 중복을 지워야하므로 set
    answer = set('A' 'B' 'C')
    # puzzle = [list(map(str, input())) for _ in range(100)]
    # zip_puzzle = list(map(list, zip(*puzzle)))
    # print(puzzle)
    # print(zip_puzzle)
    # # 글자 1개인 건 다 알고 있음. 길이 2부터 탐색
    #
    # # 생각해보니 i 도 100 까지 가야하지 않을까?
    # # for i in range(1, 50):
    # #     for row in range(100):
    # #         for col in range(100):
    # #             new_row = row + i
    # #             new_col = col + i
    # #             if new_col < 100 and new_row < 100:
    # #                 half = len(puzzle[row][col:new_col]) // 2
    # #
    #
    #
    # # 중복 조합
    # for i in range(2, 101):
    #     for cwr in combinations_with_replacement(['A', 'B', 'C'], i):
    #         half = round(i/2, 0)
    #
    #         print(half)
    #         # for idx in range(100):
    #         #     if cwr in puzzle[idx] or cwr in zip_puzzle[idx]:
    #         #         answer.add(cwr)
    #         print(cwr)
    # print(answer)
    # print(len(answer))
    # 외않되 ㅠ


    print(f'#{t} {answer}')