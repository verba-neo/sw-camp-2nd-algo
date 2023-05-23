import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    N, M = map(int,input().split())
    numbers = list(map(int, input().split()))
    sumlist = []

    # # create prefix sum list
    # tmp = 0
    # for n in numbers:
    #     tmp = tmp + n
    #     sumlist.append(tmp)
    #
    # # jogune matnun sum
    # maxsum = 0
    # minsum = sumlist[-1]
    # print(maxsum,minsum)
    # for idx in range(M,N):
    #     result = sumlist[idx] - sumlist[idx-M]
    #     if result > maxsum:
    #         maxsum = result
    #     if result < minsum:
    #         minsum = result
    # print(sumlist)
    # print(maxsum, minsum)
    # print(maxsum - minsum)

    for i in range(N):
        if i+M > N:
            break
        else:
            sumlist.append(sum(numbers[i:i+M]))

    maxsum = max(sumlist)
    minsum = min(sumlist)

    print(f'#{t} {maxsum - minsum}')