import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    numbers = list(map(int, input().split()))

    minimum = maximum = numbers[0]

    for num in numbers:
        if num < minimum:
            minimum = num
        elif num > maximum:
            maximum = num

    ans = maximum - minimum

    print(f'#{tc} {ans}')
