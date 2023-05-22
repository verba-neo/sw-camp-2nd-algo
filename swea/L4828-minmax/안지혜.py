import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    a_ls = list(map(int, input().split()))

    answer = max(a_ls) - min(a_ls)

    print(f'#{tc} {answer}')
