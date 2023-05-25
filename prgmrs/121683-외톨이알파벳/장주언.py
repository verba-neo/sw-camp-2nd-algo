
def solution(input_string):

    char_dict = {}
    answer_list = []

    for idx, char in enumerate(input_string):
        if char not in char_dict:
            char_dict[char] = [idx]
        else:
            char_dict[char].append(idx)

    for alphabet, idx_list in char_dict.items():
        if len(idx_list) >= 2:
            for i in range(len(idx_list) -1):
                if idx_list[i] - idx_list[i+1] >= 0:
                    if (idx_list[i] - idx_list[i + 1]) > 1:
                        answer_list.append(alphabet)
                        break

                if idx_list[i] - idx_list[i+1] < 0:
                    if -(idx_list[i] - idx_list[i + 1]) > 1:
                        answer_list.append(alphabet)
                        break

    if answer_list == []:
        answer = 'N'
    else:
        answer = ''.join(sorted(answer_list))

    return answer



# 'de'
print(solution("edeaaabbccd"))

# 'e'
print(solution("eeddee"))

# 'N'
print(solution("string"))

# 'bz'
print(solution("zbzbz"))