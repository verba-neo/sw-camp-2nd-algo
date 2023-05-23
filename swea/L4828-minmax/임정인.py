import sys
sys.stdin = open('./input.txt')

T = int(input())

for tc in range(1, T+1):
    input()
    # '띄어쓰기' 있을 때만 split
    i = list(map(int, input().split(" ")))
    answer = max(i) - min(i)

    print(f'#{tc} {answer}')
