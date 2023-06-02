# 열에 1과 2만 존재할 경우는 count x
# 열에 2와 1 순으로 존재할 경우 count x
# 열에 1과 2 순으로 존재할 경우 count +1
# 예를 들어 1 2 2 순이어도 count +1 / 1 2 2 2 여도 count +1
# 그러므로 무조건 1이 먼저 등장하고 2가 나와야한다.
import sys
sys.stdin = open('./input.txt')


T = 10

for tc in range(1, T+1):
    # 100 고정이긴한데 매번 입력된다.
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 서로 다른 극이 부딪힘
    hit = 0

    # 0,0에서 시작할건데 row부터 순회시킬거
    for col in range(N):
        # magnetic 1이 들어오면 추가해줄 스택
        magnetic = []
        # 한 열을 순회 시작
        for row in range(N):
            # magnetic에 아무것도 없고 1이면
            if not magnetic and matrix[row][col] == 1:
                # magnetic에 1 추가
                magnetic.append(1)
            # magnetic에 값이 있고 2라면
            elif magnetic and matrix[row][col] == 2:
                # magnetic 팝해주고
                magnetic.pop()
                # 한번 부딪힘
                hit += 1

    print(f'#{tc} {hit}')


