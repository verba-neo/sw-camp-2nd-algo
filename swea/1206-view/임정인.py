import sys
sys.stdin = open('./input.txt')

for tc in range(1, 11):  # 케이스 수
    N = int(input())  # 건물의 개수
    val = list(map(int, input().split()))  # N개의 건물의 높이
    ans = 0

    for i in range(2, N-2):
        def_2 = val[i] - val[i-2]
        def_1 = val[i] - val[i-1]
        def1 = val[i] - val[i+1]
        def2 = val[i] - val[i+2]

        if def_2 > 0 and def_1 > 0 and def1 > 0 and def2 > 0:
            ans += min(def_2, def_1, def1, def2)

    print(f'#{tc} {ans}')
