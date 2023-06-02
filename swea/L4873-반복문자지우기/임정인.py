# stack 이 편할 것

import sys
sys.stdin = open('input.txt')

# 테스트 데이터 개수
T = int(input())  # 3

for tc in range(1, T+1):

    N = list(map(str, input()))
    stack = []

    for i in range(len(N)):  # 5 / 10 / 21
        # stack 이 비어있다면
        if not stack:
            stack.append(N[i])

        else:
            # stack 에서의 마지막 원소와 동일하면
            if stack[-1] == N[i]:
                # 마지막 값 삭제
                stack.pop()
            else:
                # stack 에서의 마지막 원소와 동일하지 않으면, stack 에 추가
                stack.append(N[i])

    answer = len(stack)

    print(f'#{tc} {answer}')
