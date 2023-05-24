import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):

    A, B = map(str, input().split())
    re_A = A.replace(B, '_')

    print(f'#{t} {len(re_A)}')
