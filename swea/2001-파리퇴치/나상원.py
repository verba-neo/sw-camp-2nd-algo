import sys
sys.stdin = open(('./input.txt'))

T = int(input())


def fly_catch(j, i):
    result = 0

    for y in range(M):
        for x in range(M):
            result += board[i + y][j + x]
    catch.append(result)


for tc in range(1, T+1):
    N, M = map(int, input().split())
    board = []
    for n in range(N):
        board.append(list(map(int, input().split())))

    catch = []

    for i in range(N-M+1):
        for j in range(N-M+1):
            fly_catch(j, i)

    print(f'#{tc} {max(catch)}')