import sys
sys.stdin = open('input.txt')

T = int(input())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
direction = 0

from collections import deque

# 테스트 케이스 확인 잘 합시다🙂
for t in range(1, T+1):
    answer = 0
    N = int(input())
    maze_list = [str(input()) for _ in range(N)]

    # 결과 9/10 - 그냥 틀림

    # maze 만드는 김에 2 찾아서 해당 index x2, y2 에 저장
    maze = []
    x2, y2 = 0, 0
    for init_y in range(len(maze_list)):
        y = []
        for init_x in range(len(maze_list[0])):
            y.append(int(maze_list[init_y][init_x]))
            if maze_list[init_y][init_x] == '2':
                x2, y2 = init_x, init_y
        maze.append(y)
    # print(x2, y2)

    # x2, y2 부터 deque 에 넣고 4가지 방향을 탐색
    q = deque()
    q.append([x2, y2])
    while q:
        # print(q)
        xy = q.popleft()
        x, y = xy
        # 먼저 현재 위치(x, y)에서 4가지 방향을 탐색하며,
        # 탐색 위치가 범위를 벗어나거나
        # 탐색위치가 1이나 2라면 버리고 0이거나 3이면 deque 에 넣고 다음에 사용할 수 있도록
        for i in range(4):
            new_x, new_y = x+dx[i], y+dy[i]
            if new_x >= 0 and new_x < N and new_y >= 0 and new_y < N and maze[new_y][new_x] != 1 and maze[new_y][new_x] != 2:
                q.append([new_x, new_y])

        # 현재 위치(x, y)가 0인지 3인지 확인.
        # 0이면 다녀갔다는 기록으로 벽으로 만들어버리기.
        # 3이면 answer 을 1로 바꾸고 while 문을 끝내기.
        if maze[y][x] == 0:
            maze[y][x] = 1
        elif maze[y][x] == 3:
            answer = 1
            break

    print(f'#{t} {answer}')
