import sys

sys.stdin = open('./input.txt')


def nonrepeat(text):

    stack = []

    for char in text:
        if not stack:
            stack.append(char)

        else:
            if char == stack[-1]:
                stack.pop()
            else:
                stack.append(char)

    return len(stack)


T = int(input())

for tc in range(1, T+1):
    text = list(map(str, input()))

    # print(f'#{tc} {nonrepeat(text)}')
    print(f'#{tc} {nonrepeat(text)}')