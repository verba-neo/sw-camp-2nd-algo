import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    heights = list(map(int, input().split()))

    max_height = max(heights)

    buildings = [[0]*max_height for _ in range(len(heights))]

    for r in range(len(buildings)):
        for c in range(heights[r]):
            buildings[r][c] = 1

    great_view_room = 0
    for x in range(len(buildings)):
        for y in range(max_height):
            if buildings[x][y] != 1:
                break
            else:
                if buildings[x-1][y] == 0 and buildings[x-2][y] == 0 and buildings[x+1][y] == 0 and buildings[x+2][y] == 0:
                    great_view_room += 1

    answer = great_view_room

    print(f'#{tc} {answer}')
