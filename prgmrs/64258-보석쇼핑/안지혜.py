# 극악의 효율성. 2n으로 최적화 필요.

def solution(gems):
    gem_len = len(gems)
    gem_set = list(set(gems))
    gem_set_len = len(gem_set)
    start_idx = 0
    end_idx = 0
    added_range = 0

    # set 길이만큼 처음부터 순서대로 자름
    # 안되면 +1 해서 자름

    while True:
        # 자르는 길이 계산해서 루프 만듦
        for idx in range(gem_len-gem_set_len-added_range+1):

            gem_set = list(set(gems))
            for i in range(gem_set_len+added_range):

                if gems[idx+i] in gem_set:
                    gem_set.remove(gems[idx+i])

                    if not gem_set:
                        start_idx = idx
                        end_idx = idx+i
                        return [start_idx+1, end_idx+1]

        added_range += 1


# [3, 7]
print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
# [1, 3]
print(solution(["AA", "AB", "AC", "AA", "AC"]))
# [1, 1]
print(solution(["XYZ", "XYZ", "XYZ"]))
# [1, 5]
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
