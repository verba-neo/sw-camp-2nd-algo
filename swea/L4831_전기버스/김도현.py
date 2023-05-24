import sys
sys.stdin = open('input.txt')

T = int(input())


for t in range(1, T+1):
    K, N, M = map(int, input().split())

    answer = 0

    chrg_st = list(map(int, input().split()))
    chrg_st.reverse()

    station = list(range(0, N+1))
    print('c', chrg_st, 's', station)
    location = 0
    c_able = True
    while location < N and c_able == True:
        if location+K >= N:
            break

        if c_able:
            c_able = False
            for c in chrg_st:
                print(c, station[location+1:location+K+1])
                if c in station[location+1:location+K+1]:
                    location = c
                    answer += 1
                    c_able = True
                    break
        # # else 가 없어도 될 것 같음.
        # else:
        #     answer = 0
        #     break

    if not c_able:
        answer = 0
        # print(f'#{t} {answer}, {location}')
        print(f'#{t} {answer}')
    else:
        # print(f'#{t} {answer}, {location}')
        print(f'#{t} {answer}')
