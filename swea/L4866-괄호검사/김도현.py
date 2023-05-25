import sys
sys.stdin = open('input.txt')

T = int(input())


for t in range(1, T+1):
    string = input()
    answer = 0

    gwalho = ''

    for s in string:
        if s in "{}()[]":
            gwalho += s

    while gwalho:
        if not gwalho:
            break
        elif '{}' in gwalho:
            gwalho = gwalho.replace('{}', '')
            answer = 1
        elif '()' in gwalho:
            gwalho = gwalho.replace('()', '')
            answer = 1
        elif '[]' in gwalho:
            gwalho = gwalho.replace('[]', '')
            answer = 1
        # 그냥 else 라고 해도 될듯
        elif gwalho:
            answer = 0
            break

    print(f'#{t} {answer}')

    # 스택으로 어케 푸나염
