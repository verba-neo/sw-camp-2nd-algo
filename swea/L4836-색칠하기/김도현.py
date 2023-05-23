import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    grid = [[0]*10 for _ in range(10)]

    N = int(input())
    painting_list = [list(map(int, input().split())) for _ in range(N)]

    for area in painting_list:
        start = [area[0], area[1]]
        end = [area[2], area[3]]
        color = area[4]
        for y in range(start[0], end[0] +1 ):
            for x in range(start[1], end[1] +1 ):
                if grid[y][x] == 0 or grid[y][x] == color:
                    grid[y][x] = color
                elif grid[y][x] != color or grid[y][x] != 3:
                    grid[y][x] = 3

    answer = 0
    for g in grid:
        answer += g.count(3)

    # print(grid)
    print(f'#{t} {answer}')


# 1. set 을 이용해 교집합을 만들어 사용하는 방법
