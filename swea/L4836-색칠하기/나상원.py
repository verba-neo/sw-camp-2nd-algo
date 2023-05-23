import sys
sys.stdin = open('./input.txt')

T = int(input())

for tc in range(1, T + 1):
    # 사각형 개수
    N = int(input())

    # [0] 으로 된 2차원 배열 10 * 10 생성
    board = [[0] * 10 for _ in range(10)]
    # 보라색 개수 초기화
    pur_boxes = 0

    for boxes in range(N):
        rect = list(map(int, input().split()))
        for row in range(rect[0], rect[2]+1):
            for col in range(rect[1], rect[3]+1):
                board[row][col] += rect[4]

    for row in range(10):
        for col in range(10):
            if board[row][col] == 3:
                pur_boxes += 1


    print(f'#{tc} {pur_boxes}')
