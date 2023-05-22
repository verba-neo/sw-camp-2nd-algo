import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    card_ls = input()

    card_dict = {card: card_ls.count(card) for card in card_ls}

    card_num_answer = 0
    count_answer = 0

    for card_num, count in card_dict.items():

        if count > count_answer:
            count_answer = count
            card_num_answer = card_num

        elif count == count_answer:
            if card_num > card_num_answer:
                card_num_answer = card_num

    print(f'#{tc} {card_num_answer} {count_answer}')
