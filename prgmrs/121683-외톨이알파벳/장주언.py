
def solution(input_string):
    # 알파벳 딕셔너리
    char_dict = {}
    # 답을 넣을 곳
    answer_lst = []
    # enumerate
    for idx, char in enumerate(input_string):
        # 알파벳 딕셔너리에 char가 없으면 새로 갱신
        if char not in char_dict:
            # idx 값 추가
            char_dict[char] = [idx]
        else:
            # char가 있으면 idx값 추가
            char_dict[char].append(idx)

    for alphabet, idx_lst in char_dict.items():
        # idx값의 길이가 2이상이면 두 번 넘게 나온것
        if len(idx_lst) >= 2:
            # 음수,양수 일경우 두가지 다 설정 해줘야 답이나온다.
            for i in range(len(idx_lst) -1):
                if idx_lst[i] - idx_lst[i+1] >= 0:
                    if (idx_lst[i] - idx_lst[i + 1]) > 1:
                        answer_lst.append(alphabet)
                        break

                if idx_lst[i] - idx_lst[i+1] < 0:
                    if -(idx_lst[i] - idx_lst[i + 1]) > 1:
                        answer_lst.append(alphabet)
                        break
    # 답이 공백이면 N
    if answer_lst == []:
        answer = 'N'
    # 아니면 소트해서 출력
    else:
        answer = ''.join(sorted(answer_lst))

    return answer



# 'de'
print(solution("edeaaabbccd"))

# 'e'
print(solution("eeddee"))

# 'N'
print(solution("string"))

# 'bz'
print(solution("zbzbz"))