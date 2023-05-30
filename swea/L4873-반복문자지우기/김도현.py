import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):

    string = input()
    stack = [string[0]]

    for s in string[1:]:
        if stack:
            tmp = stack.pop()
            if tmp == s:
                continue
            elif tmp != s:
                stack.append(tmp)
                stack.append(s)
        else:
            stack.append(s)

    print(f'#{t} {len(stack)}')
