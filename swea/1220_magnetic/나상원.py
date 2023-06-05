import sys
sys.stdin = open('./input.txt')

# T = int(input())
T = 10

for tc in range(1, T+1):
    size = int(input())
    table = [list(map(int, input().split())) for _ in range(size)]

    count = 0

    for col in range(size):
        flag = 0
        for row in range(size):
            if table[row][col] == 1:
                if flag == 0 or flag == 2:
                    flag = 1
            elif table[row][col] == 2:
                if flag == 1:
                    flag = 2
                    count += 1
            else:
                if flag == 2:
                    flag = 0

    print(f'#{tc} {count}')
