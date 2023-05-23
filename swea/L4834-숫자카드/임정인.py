import sys
sys.stdin = open('./input.txt')

# 테스트 케이스 수
T = int(input())

for tc in range(1, T+1):

    N = int(input()) # 숫자 카드 개수
    num = input()

    count = [0]*10
    for i in num:
        count[int(i)] += 1

    maxx = 0
    idx = 0
    for j in range(len(count)):
        if maxx <= count[j]: # 카드 장수가 같을 때는 더 큰 숫자로 갱신
            maxx = count[j]
            idx = j

    print(f'#{tc} {idx} {maxx}')
