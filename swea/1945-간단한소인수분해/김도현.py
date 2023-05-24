import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    number = int(input())
    nanugi = [2, 3, 5, 7, 11]
    nanugilist = []
    while number > 1:
        # print(number)
        for n in nanugi:
            if number % n == 0:
                nanugilist.append(n)
                number //= n
    a = nanugilist.count(2)
    b = nanugilist.count(3)
    c = nanugilist.count(5)
    d = nanugilist.count(7)
    e = nanugilist.count(11)

    print(f'#{t} {a} {b} {c} {d} {e}')