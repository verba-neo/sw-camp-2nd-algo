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

    # max_sum = max(sumlist)
    # min_sum = min(sumlist)

    # 이 max min도 L4828 과 같이 하나의 for 문으로 O(N) 으로 해결할 수 있다.
    max_sum = -float('INF')
    min_sum = float('INF')
    for i in sumlist:
        if i >= max_sum:
            max_sum = i
        # 여기서 elif i <= min_sum: 을 하면 첫번째 케이스가 -inf 가 나와버림.
        if i <= min_sum:
            min_sum = i

    print(f'#{t} {max_sum - min_sum}')