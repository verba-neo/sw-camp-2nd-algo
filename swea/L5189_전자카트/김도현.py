import sys
sys.stdin = open('input.txt')

T = int(input())

from itertools import permutations

for t in range(1, T+1):
    N = int(input())
    sections = [list(map(int, input().split())) for _ in range(N)]
    # print(sections)

    # 순열
    # 방문 구역을 무작위로 순열. 처음이 정해져 있으므로, N-1
    tmp = [i for i in range(1, N)]
    permu_list = permutations(tmp, N-1)
    # print(tmp)

    min_waste = float("INF")

    for permu in permu_list:
        total = 0
        # 시작은 0부터
        current = 0

        # 각 조합의 구역을 꺼내면서 section[현재구역][이동할구역]으로 배터리 소모량을 total에 저장하고
        # 현재구역(current)를 이동할 구역(p)으로 변경
        for p in permu:
            total += sections[current][p]
            current = p

        # 마지막으로 출발 구역으로 돌아와야하므로, 마지막에 방문한 구역(current)에서 0까지 배터리 소모량 더하기
        total += sections[current][0]

        if total < min_waste:
            min_waste = total

    print(f'#{t} {min_waste}')
