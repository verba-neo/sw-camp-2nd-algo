import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    N = int(input())
    L = list(map(int, input().split()))

    # max_num = max(L)
    # min_num = min(L)

    # max min 을 내장 max min 을 사용하지 않으면. 효율이 조금 더 좋아질 수도 있다.
    # 내장 함수는 max min 을 모두 순회하기 때문에, O(2N) 이다.
    # 하지만 내가 for 문으로 돌면서 짜면 O(N) 이기 때문에 조오금 더 효율적이다!
    max_num = 0
    min_num = L[0]
    for i in L:
        if i >= max_num:
            max_num = i
        if i <= min_num:
            min_num = i

    print(f'#{t} {max_num - min_num}')
