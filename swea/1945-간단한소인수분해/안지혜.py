import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):

    N = int(input())

    num_alpha_dict = {
        2: 'a',
        3: 'b',
        5: 'c',
        7: 'd',
        11: 'e',
    }
    alpha_count_dict = {
        'a': 0,
        'b': 0,
        'c': 0,
        'd': 0,
        'e': 0,
    }

    for num, alpha in num_alpha_dict.items():
        while not N % num:
            if N % num == 0:
                alpha_count_dict[alpha] += 1
                N /= num

    alpha_int_list = alpha_count_dict.values()
    answer = ' '.join(list(map(str, alpha_int_list)))

    print(f'#{tc} {answer}')
