import sys
sys.stdin = open('input.txt')

T = int(input())

def check_pzl(one_line):
    tmp = 0
    for idx in range(0, N-K+1):
        if sum(one_line[idx:idx+K]) == K:
            # print(one_line[idx+K])
            if idx+K < N:
                if one_line[idx+K] == 0:
                    if idx == 0:
                        tmp += 1
                    elif one_line[idx - 1] == 0:
                        tmp += 1
                # else:
                #     break
            else:
                if one_line[idx-1] == 0:
                    tmp += 1
            # print(one_line, one_line[idx:idx+K], tmp)
        # print(tmp)
    return tmp


for t in range(1, T+1):
    answer = 0

    N, K = map(int, input().split())

    puzzle = []
    for i in range(N):
        puzzle.append(list(map(int, input().split())))

    zip_puzzle = list(map(list, zip(*puzzle)))

    if N == K:
        for line in puzzle:
            if sum(line) == N:
                answer += 1
        for z_line in zip_puzzle:
            if sum(z_line) == N:
                answer += 1
    else:
        for idx in range(len(puzzle)):
            result = check_pzl(puzzle[idx])
            zip_result = check_pzl(zip_puzzle[idx])
            answer += result + zip_result
            # answer += result
            # answer += zip_result

    print(f'#{t} {answer}')


# 흰 칸의 갯수를 세어가면서 구하는 방법도 있음.
# 흰 칸의 갯수가 N 보다 크면 X, 검은칸이 나오면 끝내고 카운트 체크
# for 문을 체크하기 위해 한 번 해보자.