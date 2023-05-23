import sys
sys.stdin = open('./input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    # 퍼즐 List
    puzzle_list = [list(map(int, input().split())) for _ in range(N)]

    puzzle_cnt = 0
    # 퍼즐 2차 List
    for puz in range(N):
        puzzle_list.append(list(map(int, input().split())))

    # 가로 '1'의 개수 세기
    for row_idx in range(N):
        count_row_1 = 0

        for col_idx in range(N):
            if puzzle_list[row_idx][col_idx] == 1:
                count_row_1 += 1
            # puzzle_list 의 값이 '0' 이거나 마지막 인덱스 값을 만났을 때 
            # '1'의 개수가 K 값과 같으면 puzzle_list 에 '1'을 더해줌
            # 아니면 '1'의 개수를 초기화
            if puzzle_list[row_idx][col_idx] == 0 or col_idx == N - 1:
                if count_row_1 == K:
                    puzzle_cnt += 1
                count_row_1 = 0
    # 세로 '1'의 개수 및 1의 개수가 K 값이면 puzzle_cnt 에 1을 더한다
    for col_idx in range(N):
        count_col_1 = 0

        for row_idx in range(N):
            if puzzle_list[row_idx][col_idx] == 1:
                count_col_1 += 1

            if puzzle_list[row_idx][col_idx] == 0 or row_idx == N - 1:
                if count_col_1 == K:
                    puzzle_cnt += 1
                count_col_1 = 0

    print(f'#{tc} {puzzle_cnt}')
