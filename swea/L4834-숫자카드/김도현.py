import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    N = int(input())
    cards = str(input())
    cdict = {}
    for c in cards:
        cdict[c] = cards.count(c)

    sorting = sorted(cdict, reverse=True)

    maxk = sorting[0]
    maxv = cdict[sorting[0]]
    for k in sorting:
        if cdict[k] > maxv:
            maxv = cdict[k]
            maxk = k

    print(f'#{t} {maxk} {maxv}')
