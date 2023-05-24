import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    M = [list(map(int, input().split())) for i in range(N)]

    red_areas = []
    blue_areas = []
    for area in M:
        if area[len(area)-1] == 1:
            red_areas.append(area)
        else:
            blue_areas.append(area)

    # color2 red: set
    red_area_set = set()
    for red_area in red_areas:
        start_r = red_area[0]
        start_c = red_area[1]
        end_r = red_area[2]
        end_c = red_area[3]

        for r in range(start_r, end_r+1):
            for c in range(start_c, end_c+1):
                red_area_set.add((r, c))

    # color2 blue: set
    blue_area_set = set()
    for blue_area in blue_areas:
        start_r = blue_area[0]
        start_c = blue_area[1]
        end_r = blue_area[2]
        end_c = blue_area[3]

        for r in range(start_r, end_r + 1):
            for c in range(start_c, end_c + 1):
                blue_area_set.add((r, c))

    # blue set, red set common area
    common_area = red_area_set & blue_area_set
    answer = len(common_area)

    print(f'#{tc} {answer}')
