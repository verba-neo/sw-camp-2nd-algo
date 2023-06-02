import sys
sys.stdin = open('input.txt')

T = 10
for test_case in range(1, T+1):

    N = int(input())
    matrix = [input().split() for _ in range(N)]

    answer = 0  # 답 저장
    for col in range(N):
        flag = 0
        for row in range(N):
            if matrix[row][col] == '1':
                flag = 1
            elif flag == 1 and matrix[row][col] == '2':
                answer += 1
                flag = 0

    print(f'#{test_case} {answer}')