import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    num_ls = list(map(int, input().split()))

    num_ls.sort()
    reversed_num_ls = num_ls[:]
    reversed_num_ls.sort(reverse=True)

    # 총 개수가 짝수일 때 반복 횟수 => len(num_ls)/2 => 오름 내림이 반반씩 딱 맞게 들어감.
    # 총 개수가 홀수일 때 반복 횟수 => len(num_ls)/2 + 1 => 마지막엔 동일한 요소를 넣음. 그래서 이때는 아무 요소나 한개 넣음.
    loop_range = int((len(num_ls))/2 + 1) if len(num_ls) % 2 else int(len(num_ls)/2)

    result = []
    for i in range(loop_range):
        # 총 개수가 홀수일때만 if 실행됨. 같은 요소 가지고 있을거임.
        if reversed_num_ls[i] == num_ls[i]:
            result.append(reversed_num_ls[i])
        else:
            result.append(reversed_num_ls[i])
            result.append(num_ls[i])

    answer = ' '.join(map(str, result[:10]))

    print(f'#{tc} {answer}')