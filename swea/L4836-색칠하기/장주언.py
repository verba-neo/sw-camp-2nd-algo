# 10 x 10의 격자
# 왼쪽 위 모서리와 오른쪽 아래 모서리의 인덱스가 주어진다.
# 겹쳐지는 부분이 보라색이 되는데 그 칸수를 구하라.
# N개의 칠해질 영역의 갯수
# 왼쪽위 모서리(r1, c1) 오른쪽아래 모서리(r2, c2) 색상정보 color

import sys

sys.stdin = open('./input.txt')

T = int(input())


for tc in range(1, T + 1):
    N = int(input())
    colored = [[[] for _ in range(10)] for _ in range(10)]
    result = 0

    for i in range(N):
        r1, c1, r2, c2, color = map(int, input().split())

        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                colored[i][j].append(color)

    for i in range(10):
        for j in range(10):
            if len(colored[i][j]) == 2:
                result += 1

    print(f'#{tc} {result}')

