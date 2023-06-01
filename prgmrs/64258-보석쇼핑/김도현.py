def solution(gems):

    answer = []
    kind_gem = set(gems)

    min_list_len = len(gems)
    for idx in range(len(gems)-len(kind_gem) + 1):
        for jdx in range(idx, len(gems)+1):
            print(set(gems[idx:jdx]), kind_gem)
            if set(gems[idx:jdx]) == kind_gem:
                if len(gems[idx:jdx]) <= min_list_len:
                    if answer == []:
                        min_list_len = len(gems[idx:jdx])
                        answer = [idx + 1, jdx]
                    elif jdx - idx < answer[1] - answer[0]:
                        min_list_len = len(gems[idx:jdx])
                        answer = [idx + 1, jdx]

    return answer


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
