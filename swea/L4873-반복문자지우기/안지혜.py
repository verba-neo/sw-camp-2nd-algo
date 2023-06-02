import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = input()
    stack = []

    for char in N:
        if stack and char == stack[-1]:
            stack.pop()
        else:
            stack.append(char)

    answer = len(stack)
    print(f'#{tc} {answer}')
