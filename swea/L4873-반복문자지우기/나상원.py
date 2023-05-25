import sys
sys.stdin = open('./input.txt')

T = int(input())

for tc in range(1, T+1):
    string = list(input())
    s_stack = []

    for char in string:
        if s_stack and char == s_stack[-1]:
            s_stack.pop()
        else:
            s_stack.append(char)

    answer = len(s_stack) if len(s_stack) != 0 else 0

    # if len(s_stack) == 0:
    #     answer = 0

    print(f'{tc} {answer}')
