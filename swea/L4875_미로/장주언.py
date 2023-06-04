import sys

sys.stdin = open('./input.txt')

T = int(input())

for tc in range(1, T+1):
    # 테두리
    N = int(input())

    # 미로
    maze = [list(map(int, list(input()))) for _ in range(N)]
    # print(maze)

    # row와 col을 0으로 설정 해주고
    row, col = 0, 0

    # 3을 만나는가 못 만나는가에 따라 변해 줄 result
    result = 0

    # 이동할 방향 상하좌우
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # 출발점 찾기
    for i in range(N):
        # 2가 들어 있는 row
        if 2 in maze[i]:
            # 해당 row에서 col의 위치
            col = maze[i].index(2)
            row = i
            # 찾으면 브레이크
            break
    # 스택을 만들고, 첫 row, col 값을 입력
    stack = [(row, col)]

    # 스택이 비어있을때까지 반복
    while stack:
        # 출발 좌표를 pop
        row, col = stack.pop()
        # 미로에서 돌아가지 못하게 1로 바꿔준다.
        maze[row][col] = 1
        # 4방향을 탐색할건데,
        for d_row, d_col in directions:
            nxt_row = row + d_row
            nxt_col = col + d_col

            # 진행이 불가능한 영역이면 다음으로
            if nxt_row < 0 or nxt_col < 0 or nxt_row >= N or nxt_col >= N:
                continue
            # 만약 3에 도착한다면
            if maze[nxt_row][nxt_col] == 3:
                # result 를 1로 바꾸고 종료
                result = 1
                break
            # 0을 만났을 때, 해당 좌표를 스택에 추가
            elif not maze[nxt_row][nxt_col]:
                stack.append((nxt_row, nxt_col))

            # 반복해서 다 탐색
    print(f'#{tc} {result}')