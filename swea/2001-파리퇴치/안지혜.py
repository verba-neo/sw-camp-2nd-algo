import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N_M = input().split()
    N = int(N_M[0])
    M = int(N_M[1])

    boxes = []
    for i in range(N):
        boxes.append(list(map(int, input().split())))

    caught_flies_list = []
    for r in range(N-M+1):
        for c in range(N-M+1):
            swatter_boxes = []
            for swatter_r in range(M):
                for swatter_c in range(M):
                    swatter_boxes.append(boxes[r+swatter_r][c+swatter_c])

            caught_flies_list.append(sum(swatter_boxes))

    answer = max(caught_flies_list)

    print(f'#{tc} {answer}')
