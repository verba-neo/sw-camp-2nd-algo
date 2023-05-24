import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    N = int(input())
    L = list(map(int, input().split()))

    maxnum = max(L)
    minnum = min(L)

    print(f'#{t} {maxnum - minnum}')