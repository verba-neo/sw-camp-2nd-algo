import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N_Q = input().split()
    N = int(N_Q[0])
    Q = int(N_Q[1])

    LRs = []
    for i in range(Q):
        L_R = input().split()
        LRs.append(list(map(int, L_R)))

    boxes = [0] * N
    for i, LR in enumerate(LRs):
        L = LR[0]
        R = LR[1]
        for idx in range(R-L+1):
            boxes[L+idx-1] = i+1

    answer = ' '.join(list(map(str, boxes)))

    print(f'#{tc} {answer}')
