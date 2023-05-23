import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    N, Q = map(int, input().split())

    nlist = [0] * N
    for q in range(1, Q+1):
        L, R = map(int, input().split())
        for idx in range(L-1,R):
            nlist[idx] = q

    result = ' '.join(map(str,nlist))
    print(f'#{t} {result}')