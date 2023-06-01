import sys
sys.stdin = open('input.txt')

T = int(input())

from itertools import permutations

for t in range(1, T+1):
    N = int(input())
    sections = [list(map(int, input().split())) for _ in range(N)]
    print(sections)
    answer = 0

    tmp = [i for i in range(1, N)]
    permu_list = permutations(tmp, N-1)
    print(tmp)

    min_waste = float("INF")

    for permu in permu_list:
        total = 0
        current = 0

        for p in permu:
            total += sections[current][p]
            current = p

        total += sections[current][0]

        if total < min_waste:
            min_waste = total



    print(f'#{t} {min_waste}')