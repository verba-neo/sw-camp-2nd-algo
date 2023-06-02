def solution(gems):
    # answer = []
    minimum = len(gems)
    gems_set_size = len(set(gems))
    gems_slic = [1, len(gems)]

    for slice_idx in range(len(gems)-gems_set_size+1):
        for idx in range(slice_idx+gems_set_size, len(gems)+1):
            pick_gems = gems[slice_idx:idx]
            if len(set(gems[slice_idx:idx])) == gems_set_size and len(pick_gems) < minimum:
                minimum = len(pick_gems)
                gems_slic[0] = slice_idx+1
                gems_slic[1] = idx

    return gems_slic


# gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]

# print(solution(gems))

# [3, 7]
print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
# [1, 3]
print(solution(["AA", "AB", "AC", "AA", "AC"]))
# [1, 1]
print(solution(["XYZ", "XYZ", "XYZ"]))
# [1, 5]
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
