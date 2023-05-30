def solution(input_string):
    char_dict = {}

    # 딕셔너리 생성. key = 알파벳, value = [인덱스]
    for idx, char in enumerate(input_string):
        if char_dict.get(char):
            char_dict[char] = char_dict[char] + [idx]
        else:
            char_dict.setdefault(char, [idx])

    alphas = []
    for alpha, indexes in char_dict.items():
        index_count = len(indexes)

        if index_count >= 2:
            first_index = indexes[0]
            for i, index in enumerate(indexes):
                # 연속되지 않은 알파벳은 alphas에 넣을 것임. 첫번째 인덱스는 넘기고, 두번째 인덱스부터 연속된 숫자인지 체크
                if index != first_index and index != first_index+i:
                    alphas.append(alpha)
                    break
    alphas.sort()

    answer = ''.join(alphas) if alphas else 'N'
    return answer






# 'de'
print(solution("edeaaabbccd"))

# 'e'
print(solution("eeddee"))

# 'N'
print(solution("string"))

# 'bz'
print(solution("zbzbz"))
