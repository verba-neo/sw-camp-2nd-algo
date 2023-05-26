# 가로세로 길이가 10x20, 20x20인 직사각형 종이들

# 20xN을 표시하고

# 직사각형으로 채울 때, 경우의 수

# 10 과 20이 경우의 가장 기본 수

# 모든 수는 10과 20으로 표현이 가능

# 추가되는 경우의 수는 전수에서 10과 20을 더한것

# 그러므로 An-1에 10을 더한것과 An-2에 20을 더한 것이 있다.

# 그런데 An-1과 An-2에 끝에 10 10을 포함한다면 같은 표현이므로 삭제.

# 10이들어가면 x1 20이들어가면 x2가 된다.

# An-1 x1 과  An-2 x2가된다.
import sys

sys.stdin = open('./input.txt')


def cases(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3

    return cases(n-1) + 2 * cases(n-2)


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    n = N//10

    print(f'#{tc} {cases(n)}')
