# N x N 크기의 단어 퍼즐
# 주어진 퍼즐 모양에서 특정 길이의 단어 K
# 0은 검은색, 1은 흰색

import sys

sys.stdin = open('./input.txt')

T = int(input())

for tc in range(1, T + 1):

    N, K = map(int, input().split())

    puzzles = [list(map(int, input().split())) for _ in range(N)]

    count = 0

    for i in range(N):
        word_length = 0
        for j in range(N):

            if puzzles[i][j] == 1:
                word_length += 1

            if puzzles[i][j] == 0 or j == N - 1:
                if word_length == K:
                    count += 1
                word_length = 0

        for j in range(N):

            if puzzles[j][i] == 1:
                word_length +=1
            if puzzles[j][i] == 0 or j == N - 1:
                if word_length == K:
                    count += 1
                word_length = 0

    print(f'#{tc} {count}')

