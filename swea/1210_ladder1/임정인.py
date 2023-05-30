import sys
sys.stdin = open('./input.txt')

# 답이 안 나와...

# 테스트 데이터 개수
T = 10


# 도착 지점에서 거꾸로 올라가기
for tc in range(1, T+1):

    N = int(input())
    num = [list(map(int, input().split())) for _ in range(100)]  # 100 * 100줄

    # 0:왼쪽, 1:오른쪽, 2:위 (무조건 올라가는 것부터 시작)
    # 델타 이동
    dr = [0, 0, -1]
    dc = [-1, 1, 0]


    # 도착점 col idx 구하기
    for x in range(100):
        if num[99][x] == 2:
            col = x

    # row = 99
    # col = num[row].index(2)

    # 방향 위로 초기화
    direction = 2  # 0:왼쪽, 1:오른쪽, 2:위
    row = 99

    while True:
        # row == 0 이 되면 종료
        if row == 0:
            break

        # 왼쪽에 1이 있으면 왼쪽으로 가다가 0 나오면 종료
        if num[row][col-1]:
            direction = 0
            while True:
                row += dr[direction]
                col += dr[direction]
                if num[row][col-1] == 0:
                    break

        # 오른쪽에 1이 있으면 오른쪽으로 가다가 0 나오면 종료
        elif num[row][col+1]:
            direction = 1
            while True:
                row += dr[direction]
                col += dr[direction]
                if num[row][col+1] == 0:
                    break
        # 위로 이동
        direction = 2
        row += dr[direction]
        col += dr[direction]

    print(f'{tc} {col-1}')


# 강사님 설명
# if col < 99 : 99에서 오른쪽으로 꺾을 일이 없음
# if col > 0 : 0에서 왼쪽으로 꺾을 일이 없음
# 왼/오 모두 갈 수 없으면 row -= 1

# if = 올라가는 도중 / else = 좌우 이동
# 좌우 이동하는 동안에는 내려가는 일 x => 올라가는 일만 O
# while row > 0 조건이 있기 때문에 else의 if문에는 따로 조건 필요하지 X

# while 문 끝났다면 row 값은 모두 0, 즉 col 값 필요하므로 -> return col
# 함수로 짜기(def) 추천 : 재귀 때 많이 사용할 예정
