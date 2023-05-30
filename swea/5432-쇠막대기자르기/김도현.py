import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    answer = 0

    rail = input()

    pipe = 0
    idx = 0
    while idx < len(rail):
        # print(rail[idx:idx+2])
        # print(rail[idx:idx+2])
        if rail[idx:idx+2] == '()':
            # 레이저임
            answer += pipe
            idx+= 1
        elif rail[idx] == '(':
            pipe += 1
        elif rail[idx] == ')':
            answer += 1
            pipe -= 1
        idx += 1


    print(f'#{t} {answer}')


    # 강사님의 풀이
    # () 를 * 로 replace 하면 막대와 레이저를 구분하기 쉬워집니다. 😲!!