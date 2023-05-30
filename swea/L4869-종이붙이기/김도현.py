import sys
sys.stdin = open('input.txt')

T = int(input())


for t in range(1, T+1):
    N = int(input())

    answer = 0

    block_stack = [0]* (N//10)

    def block(case):
        global answer
        if not block_stack:
            return
        elif case == 1:
            block_stack.pop()
            answer += 1
            block(1)
            block(2)
        elif case == 2:
            block_stack.pop()
            block_stack.pop()
            answer += 2
            block(1)
            block(2)

    block(1)
    block(2)

    print(answer)
