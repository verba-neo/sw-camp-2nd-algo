import sys
sys.stdin = open('./input.txt')

T = int(input())

# reference 값 (list .. ) 함수 스코프에 적용해도 가르키는 값이 같기 때문에 변화가 생김.

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    sort_list = []

    numbers.sort()
    for idx in range(N//2):
        sort_list.append(numbers[(N-1)-idx])
        sort_list.append(numbers[idx])

    # answer = []
    # for idx in range(10):
    #     answer.append(sort_list[idx])
    # answer_list = ' '.join(map(str, answer))
    # print(f'#{tc} {answer_list}')

    print(f'#{tc}', *sort_list[:10])
