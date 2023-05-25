import sys

sys.stdin = open('./input.txt')

T = int(input())

for tc in range(1, T+1):
    # 정수의 개수
    N = int(input())
    # 기존의 정수 리스트를 정렬
    origin_lst = sorted(list(map(int, input().split())))
    reversed_origin_lst = sorted(origin_lst, reverse=True)

    # 새롭게 정렬할 리스트
    new_lst = [0]*N
    # 1 2 3 4 5 6
    # 0 1 2 3 4 5 -> //2
    # 6 5 4 3 2 1
    # 0 1 2 3 4 5 -> //2
    # 6 1 5 2 4 3
    # 0 1 2 3 4 5

    for idx in range(N):
        if idx % 2 == False:
            new_lst[idx] = reversed_origin_lst[idx//2]
        else:
            new_lst[idx] = origin_lst[idx//2]
    result = []
    for idx in range(10):
        result.append(new_lst[idx])

    answer = ' '.join(map(str, result))



    print(f'#{tc} {answer}')