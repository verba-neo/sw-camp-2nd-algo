import sys
sys.stdin = open('input.txt')

T = int(input())

from itertools import permutations

for t in range(1, T+1):
    N = int(input())
    puzzle = [list(map(int, input().split())) for _ in range(N)]

    min_sum = float("INF")

    # 순열 결과: 9/10 - 제한시간 초과
    num = [i for i in range(N)]
    permu_list = permutations(num, N)

    for sunyul in permu_list:
        print(sunyul)
        numbers = 0
        for idx in range(len(puzzle)):
            numbers += (puzzle[idx][sunyul[idx]])
        total = numbers
        if total == N:
            min_sum = total
            break
        elif total < min_sum:
            min_sum = total

    # ?


    print(f'#{t} {min_sum}')