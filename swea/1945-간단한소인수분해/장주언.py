import sys

sys.stdin = open('./input.txt')

T = int(input())

for tc in range(1, T + 1):

    N = int(input())
    # 소인수목록생성
    pf_lst = [2, 3, 5, 7, 11]
    # 카운트할 리스트 초기화
    count_lst = [0, 0, 0, 0, 0]
    # index 범위설정
    for idx in range(len(pf_lst)):
        # N을 소인수로 나누었을 때 0이 될 때까지 반복
        while N % pf_lst[idx] == False:
            # 소인수로 나누어주고 카운트
            count_lst[idx] += 1
            # N을 소인수로 나눈 후 몫으로 다시 입력
            N = N // pf_lst[idx]
    # count_lst 타입 변화
    count = ' '.join(map(str, count_lst))

    print(f'#{tc} {count}')



