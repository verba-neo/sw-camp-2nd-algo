# # 기존 문제와 다른점
# # 이동의 제한이 없다. => 왔던 곳도 다시 갈 수 있다. => visited True False의 필요성 x
# # case의 최대갯수는??
# # 7자리를 합쳤을 때 그 총 배열이 겹치면 안된다.
# # 이동이 불가능한 영역을 들어가지않는다면 계속 돌게 만들기
# # 그 안에서 차례대로 random한  시작점을 설정후
# # 각 디렉션으로 모두 이동 총 7번 => 재귀함수를 통해 7자리를 만들면 스탑하게 만들기
# # set을 먹여서 중복값 삭제? => set에 추가해주면 중복값은 안들어가지지 않나
#
#
import sys

sys.stdin = open('./input.txt')


def dfs(digit, row, col):
    if len(digit) == 7:
        comb.add(digit)
        return

    # 시작점은 아무곳이나 가능하니까 다 탐색

        # 4방향 탐색

    for directions in range(4):

        nxt_row = row + d_row[directions]
        nxt_col = col + d_col[directions]

        if 0 <= nxt_row < N and 0 <= nxt_col < N:
            dfs(digit + str(matrix[nxt_row][nxt_col]), nxt_row, nxt_col)

    return


T = int(input())

# 상하좌우
d_row = [-1, 1, 0, 0]
d_col = [0, 0, -1, 1]


for tc in range(1, T+1):
    # 4x4 배열 매트릭스
    N = 4

    matrix = [list(map(int, input().split())) for _ in range(N)]

    comb = set()
    for y in range(N):
        for x in range(N):
            dfs('', y, x)

    answer = len(comb)

    print(f'#{tc} {answer}')


