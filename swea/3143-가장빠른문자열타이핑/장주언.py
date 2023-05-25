# 단어를 일반적으로 타이핑한다면 단어 길이만큼 타이핑 횟수
# 특정 문자열 B가 저장되어 있다면 키를 한번 눌러서 타이핑 횟수를 줄일수 있다.
# 첫번째 줄에 케이스의 수 T
# 각 케이스마다 단어 A와 특정 문자열 B가 주어진다.
# 1 <= A <= 10,000  1 <= B <= 100
# A를 타이핑하기 위해 눌러야하는 최솟값을 출력

import sys

sys.stdin = open('./input.txt')

T = int(input())

for tc in range(1, T+1):

    A, B = list(input().split())

    idx = 0

    count = 0

    while idx < len(A):

        # A[idx] 부터 A[idx+len(B)]가 B이면 count += 1
        if A[idx: idx+len(B)] == B:
            count += 1
            idx += len(B)

        # B가 아니면 count += 1, idx += 1
        else:
            count += 1
            idx += 1

    print(f'#{tc} {count}')







