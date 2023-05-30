def solution(input_string):
    answer = ''
    # 마지막으로 확인한 문자열
    last = input_string[0]
    # 기존에 등장한 적이 있는지 / 1번만 나오면 조건 불만족 (2번 이상 나오고 찢어져 있으면 해당)
    appears = [last]

    # 2 ~ 끝까지 순회
    for current in input_string[1:]:
        # 붙어있는 글자들은 할일 없음
        if current == last:
            continue
        else:
            # 기존에 등장한 적 있음, 아직 answer에는 없음
            if current in appears and current not in answer:
                answer += current
            # 처음 본 알파벳 이라면,
            else:
                appears.append(current)
                # 마지막 문자열을 지금 본 문자열로 교체
                last = current
    return ''.join(sorted(answer)) if answer else 'N'


# txt 불러와서 print 로 실행해보기!
# 'de'
print(solution("edeaaabbccd"))

# 'e'
print(solution("eeddee"))

# 'N'
print(solution("string"))

# 'bz'
print(solution("zbzbz"))