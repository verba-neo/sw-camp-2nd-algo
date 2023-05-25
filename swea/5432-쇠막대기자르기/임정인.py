import sys
sys.stdin = open('./input.txt')

# 테스트 데이터 개수
T = int(input())


# ( 개수 센 후에 레이저() 만나면 ( 개수만큼 카운트
# ) 만나면 +1 한 후, 전체 ( 개수에서 -1 : ) 나오면 2가지 일 발생

for tc in range(1, T+1):

    N = input()
    N = list(N.replace('()', '*'))

    rod = 0
    total = 0

    # 왜 idx가 있어야 for문이 실행되는지..?
    for idx, el in enumerate(N):
        if el == '(':
            rod += 1
        elif el == '*':
            total += rod

        elif el == ')':
            rod -= 1
            total += 1


    print(f'{tc} {total}')
