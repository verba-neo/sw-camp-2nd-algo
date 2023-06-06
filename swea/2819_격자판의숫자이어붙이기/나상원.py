import sys
sys.stdin = open('./input.txt')

T = int(input())


def dfs(idx, row, col, number):

    d_row = [0, 1, 0, -1]
    d_col = [1, 0, -1, 0]

    number += board[row][col]

    if idx == 6:
        answer.append(number)
        return
    for direction in range(4):
        if 0 <= row + d_row[direction] < 4 and 0 <= col + d_col[direction] < 4:
            dfs(idx+1, row+d_row[direction], col+d_col[direction], number)


for tc in range(1, T+1):
    board = [list(map(str, input().split())) for _ in range(4)]

    answer = []

    for row in range(4):
        for col in range(4):
            dfs(0, row, col, "")
    answer = len(set(answer))

    print(f'#{tc} {answer}')
