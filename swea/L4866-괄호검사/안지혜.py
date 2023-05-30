import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    string = input()
    targets = ['(', ')', '{', '}']
    history = []
    prev_el = None

    for i in range(len(string)):
        if string[i] in targets:
            if (string[i] == ')' and prev_el == '(') or (string[i] == '}' and prev_el == '{'):
                history.pop()
                prev_el = history[-1] if history else None
            else:
                history.append(string[i])
                prev_el = string[i]

    answer = 0 if history else 1

    print(f'#{tc} {answer}')