import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [[0] * 10 for _ in range(10)]

    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())

        for row in range(r1, r2+1):
            for col in range(c1, c2+1):
                # 현재 칸에 색이 칠해져 있고, 현재 칠할 색과 다르다면
                if matrix[row][col] and matrix[row][col] != color:
                    # 보라색(3)
                    matrix[row][col] = 3
                # 색이 칠해져 있지 않다면
                else:
                    # 현재 색으로 덮어쓰기
                    matrix[row][col] = color

    count = 0
    for r in range(10):
        for c in range(10):
            if matrix[r][c] == 3:
                count += 1

    print(f'#{tc} {count}')
