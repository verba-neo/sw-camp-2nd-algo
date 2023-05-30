import sys
sys.stdin = open('./input.txt')

# 테스트 데이터 개수
T = int(input())  # 3

for tc in range(1, T+1):

    N = int(input())  # 10
    num = list(map(int, input().split()))  # N개의 정수
    answer = []

    for i in range(1, N//2+1):  # 한 번 실행할 때 2개의 숫자 answer 에 저장되므로 N//2+1
        if i < N//2+1:
            num.sort(reverse = True)
            answer.append(num[0])  # 1번째 원소 answer 에 저장
            num.pop(0)  # num 에서의 idx=0 제거
            answer.append(num[-1])  # 맨 마지막 원소 answer 에 저장
            num.pop(-1)  # num 에서의 idx=-1 제거

    answer = str(answer[0:10])[1:-1]  # 10개까지만 출력 후, 문자열 변환 및 괄호 제거
    result = answer.replace(',', '')

    print(f'#{tc} {result}')

    # for i in range(1):
    #     print(*answer)

# (2) 강사님 풀이
def solution(numbers):

    sorted_numbers = []

    for _ in range(10):
        sorted_numbers.append(numbers.pop())  # pop()은 인자 없으면 기본적으로 마지막 요소 빼줌
        sorted_numbers.append(numbers.pop(0))

    return ' '.join(map(str, sorted_numbers))


T = int(input())

for tc in range(1, T+1):

    N = int(input())
    numbers = list(map(int, input().split()))
    numbers.sort()
    print(f'#{tc} {solution(numbers)}')  # 1 3 4
    # print(f'#{tc}, *soltion(numbers)') 도 가능

# 값이 비어있으면 false
# if ll : 리스트 ll이 비어있지 않다면 계속한다 = if len(ll)
# while 11 : ll 있으면
# reference 여도 immutable 해도 괜찮음 (list는 mutable이라 안 괜찮음)
# print(1, 2, 3) = print(*[1, 2, 3])
