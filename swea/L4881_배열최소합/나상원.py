import sys
sys.stdin = open('./input.txt')


def dfs(s_row):
    global part_sum, min_sum

    # 가지 치기(Pruning) => Backtracking
    # 없이 실행 해서 시간 초과 발생함..
    if min_sum < part_sum:
        return
    # s_row 가 배열의 수가 같으면,
    if s_row == N and part_sum < min_sum:
        min_sum = part_sum

    for col_idx in range(N):
        if not visited[col_idx]:
            visited[col_idx] = True
            part_sum += matrix[s_row][col_idx]
            dfs(s_row+1)
            # col 에서도 하나 만 선택이 가능 해서 비방문 처리
            visited[col_idx] = False
            # 갈림길 까지의 값을 뺴줘야함.
            part_sum -= matrix[s_row][col_idx]

    return min_sum


T = int(input())

for tc in range(1, T+1):
    N = int(input())

    matrix = [list(map(int, input().split())) for _ in range(N)]

    # print(matrix)

    # [0, 0]
    # [1, 1], [1, 2]
    # [2, 2], [2, 1]
    visited = [False for _ in range(N)]
    part_sum, min_sum = 0, 10*N

    dfs(0)

    print(f'#{tc} {min_sum}')

