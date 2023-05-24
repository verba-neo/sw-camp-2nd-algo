import sys
sys.stdin = open('./input.txt')

# 테스트 데이터 개수
T = int(input())

# 딱 K에 맞는 칸에만 단어가 들어갈 수 있다!

for tc in range(1, T+1):
    # N = 가로/세로 길이, K = 단어의 길이
    N, K = map(int, input().split())
    puzzle = []

    for t in range(N):
        puzzle.append(list(map(int, input().split())))
    answer = []

    for i in range(N):
        count = 0
        for j in range(len(puzzle[i])):
            if puzzle[i][j]:
                count += 1
            else:
                answer.append(count)
                count = 0

        answer.append(count)

    for j in range(len(puzzle[0])):
        count = 0
        for i in range(len(puzzle)):
            if puzzle[i][j]:
                count += 1
            else:
                answer.append(count)
                count = 0

        answer.append(count)

    ans = 0
    for num in answer:
        if num == K:
            ans += 1

    print(f'#{tc} {ans}')
