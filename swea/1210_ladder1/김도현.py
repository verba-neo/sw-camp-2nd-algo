import sys
sys.stdin = open('input.txt')

for t in range(1, 11):
    t = input()
    grid = [[i for i in list(map(int, input().split()))] for _ in range(100)]

    start_x = grid[99].index(2)

    d_x = [1, -1, 0]
    d_y = [0, 0, -1]
    direction = 0

    x = start_x
    y = 99

    while y > 0:
        new_x = x + d_x[direction]
        new_y = y + d_y[direction]

        if new_x >= 0 and new_x < 100 and new_y >= 0 and new_y < 100 and grid[new_y][new_x] == 1:
            x = new_x
            y = new_y
            grid[new_y][new_x] = 2
            direction = 0
        else:
            direction = (direction + 1) % 3

    end_x = grid[0].index(2)
    print(f'#{t} {end_x}')