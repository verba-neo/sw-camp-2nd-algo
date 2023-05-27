
def solution(input_string):
    answer = ''

    # 문자의 idx 를 리스트로 저장함
    char_dict = {}
    # 정렬을 해야되서 리스트로 저장
    answer_list = []

    for idx, char in enumerate(input_string):
        if char not in char_dict:
            char_dict[char] = [idx]
        else:
            char_dict[char].append(idx)

    for ch, ch_idx in char_dict.items():
        if len(ch_idx) >= 2:
            for i in range(len(ch_idx) - 1):
                if ch_idx[i+1] - ch_idx[i] > 1:
                    answer_list.append(ch)
                    break

    answer_list.sort()
    answer = ''.join(answer_list)

    if len(answer_list) == 0:
        answer += 'N'

    return answer


# 'de'
print(solution("edeaaabbccd"))

# 'e'
print(solution("eeddee"))
#
# 'N'
print(solution("string"))

# 'bz'
print(solution("zbzbz"))
