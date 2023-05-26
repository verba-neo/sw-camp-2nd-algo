from itertools import combinations_with_replacement

import sys
sys.stdin = open('input.txt')


def check_same(p, idx, jdx):
    i = 0
    while idx+i <= jdx-i:
        if p[idx+i] != p[jdx-i]:
            return False
        i += 1
    return jdx


def is_poham(checked_list, checked_word):
    for c in checked_list:
        if checked_word in c:
            return False
    return True


for t in range(1, 11):
    t = input()

    # 구간을 정해서 큰 것부터 넣고, 작은 게 큰 거에 포함되어 있으면 제외
    # 큰 것부터 돌아야하기 때문에 row 로 모두 살핀 뒤에
    # length 를 줄여야합니다.

    answer = []
    puzzle = [list(map(str, input())) for _ in range(100)]
    zip_puzzle = list(map(list, zip(*puzzle)))

    length = 99
    while length > 1:
        for row in range(100):
            pz_line = puzzle[row]
            idx = 0
            while idx + length < 100:
                if pz_line[idx] == pz_line[idx+length]:
                    tmp = ''
                    result = check_same(pz_line, idx, idx+length)
                    for p in pz_line[idx:idx+length]:
                        tmp += p
                    if not result:
                        break
                    else:
                        idx = result
                        poham_result = is_poham(answer, tmp)


                print(idx)
                idx += 1


        length -= 1







    # # 중복을 지워야하므로 set
    # answer = ['A', 'B', 'C']
    # tpuzzle = [list(map(str, start())) for _ in range(100)]
    # tzip_puzzle = list(map(list, zip(*tpuzzle)))
    #
    # for index in range(100):
    #     puzzle = tpuzzle[index]
    #     zip_puzzle = tzip_puzzle[index]
    #     idx = 0
    #     jdx = 99
    #     while idx < 100:
    #         while jdx > 1:
    #             # print(puzzle[0][idx:jdx])
    #             # # 변수 확인용
    #             # tmp = puzzle[idx:jdx+1]
    #             # ztmp = zip_puzzle[idx:jdx+1]
    #             if puzzle[idx] == puzzle[jdx]:
    #                 result = check_same(puzzle, idx, jdx)
    #
    #                 if not result:
    #                     jdx -= 1
    #                     break
    #                 else:
    #                     # print(puzzle[idx])
    #                     a = ''
    #                     for p in puzzle[idx:jdx+1]:
    #                         # print(p)
    #                         a += p
    #                     idx = jdx
    #                     jdx = 99
    #                     check_result = is_poham(answer, a)
    #                     if check_result:
    #                         answer.append(a)
    #                     break
    #
    #             if zip_puzzle[idx] == zip_puzzle[jdx]:
    #                 result = check_same(zip_puzzle, idx, jdx)
    #                 if not result:
    #                     jdx -= 1
    #                     break
    #                 else:
    #                     za = ''
    #                     for zp in zip_puzzle[idx:jdx+1]:
    #                         za += zp
    #                     idx = jdx
    #                     jdx = 99
    #                     check_result = is_poham(answer, za)
    #                     if check_result:
    #                         answer.append(za)
    #                     break
    #             jdx -= 1
    #         idx += 1
    # # answer.remove('')
    #
    # # 넘무 야매입니까? 어떻게 숫자가 같은 값이 나오지?
    # answer = list(set(answer))
    # answer.reverse()
    #
    #
    # real_answer = len(answer)
    #
    # print(f'#{t} {answer}')
    # print(f'#{t} {real_answer}')
