import sys
sys.stdin = open('input.txt')

t = int(input())

for tn in range(1, t+1):
    N, M = map(int, input().split())
    pad = []
    for n in range(N):
        pad.append(list(map(int, input().split())))


    def catch(y, x):
        count = 0
        for my in range(M):
            for mx in range(M):
                if x+mx <= N-1 and y+my <= N-1:
                    # print('좌표', pad[y+my][x+mx])
                    count += pad[y+my][x+mx]
        return count

    maxcatch = 0
    for y in range(N-M+1):
        for x in range(N-M+1):
            result = catch(y, x)
            # print('result', result)
            if result > maxcatch:
                maxcatch = result
    print(f"#{tn} {maxcatch}")

