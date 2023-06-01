import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    maze = []
    start_r = start_c = None
    answer = 0

    # 메이즈 만들고 시작점 찾기
    for i in range(N):
        maze_r = list(map(int, input()))
        if 2 in maze_r:
            start_r, start_c = i, maze_r.index(2)
        maze.append(maze_r)

    now = [start_r, start_c]
    stack = [now]

    def push_positions(r, c):
        positions = []
        directions = []
        d = [[r, c-1], [r-1, c], [r, c+1], [r+1, c]]

        if 0 < r < N-1 and 0 < c < N-1:
            directions = d
        elif 0 < r < N-1 and c == 0:
            directions = [d[1], d[2], d[3]]
        elif r == 0 and 0 < c < N-1:
            directions = [d[0], d[2], d[3]]
        elif 0 < r < N-1 and c == N-1:
            directions = [d[0], d[1], d[3]]
        elif r == N-1 and 0 < c < N-1:
            directions = [d[0], d[1], d[2]]
        elif r == 0 and c == 0:
            directions = [d[2], d[3]]
        elif r == 0 and c == N-1:
            directions = [d[0], d[3]]
        elif r == N-1 and c == N-1:
            directions = [d[0], d[1]]
        elif r == N-1 and c == 0:
            directions = [d[1], d[2]]
        for r, c in directions:
            if maze[r][c] == 0 or maze[r][c] == 3:
                positions.append([r, c])

        return positions

    while stack:
        now = stack.pop()

        if maze[now[0]][now[1]] == 3:
            answer = 1
            break
        maze[now[0]][now[1]] = 1

        stack += push_positions(*now)

    print(f'#{tc} {answer}')
