import sys
sys.stdin = open('input.txt')


def solution(numbers):
    sorted_numbers = []

    for _ in range(5):
        sorted_numbers.append(numbers.pop())  # pop() 은 인자없으면 기본적으로 마지막 요소 pop
        sorted_numbers.append(numbers.pop(0))

    # return ' '.join(map(str, sorted_numbers))
    return sorted_numbers


T = int(input())

for tc in range(1, T+1):

    N = int(input())
    numbers = list(map(int, input().split()))
    numbers.sort()
    print(f'#{tc}', *solution(numbers))  # 1 3 4
