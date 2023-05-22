import sys
sys.stdin = open(('./input.txt'))

T = int(input())

for tc in range(1, T+1):
    N, Q = map(int, input().split())

    box_list = [0] * N

    for i in range(1, Q + 1):

        L, R = map(int, input().split())
        for j in range(L - 1, R):
            box_list[j] = i

    boxes = ' '.join(map(str, box_list))

    print(f'{tc} {boxes}')
