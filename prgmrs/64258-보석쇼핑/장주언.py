# def solution(gems):
#     list_gems = set(gems)
#
#     min_list = len(gems) - len(list_gems)
#
#     buying = len(gems)
#
#     answer = (1, len(gems))
#
#     for start in range(0, min_list+1):
#
#         for end in range(len(list_gems), len(gems)):
#
#               if len(set(gems[start:end])) == len(list_gems) and (end - (start+1)) < buying:
#
#
#                         buying = (end - (start+1))
#
#                         answer = [start+1, end]
#
#
#     return answer

# def solution(gems):
#
#     N = minimum = len(gems)
#     uniq_count = len(set(gems))
#     answer = [1, N]
#
#     for start in range(0, N-uniq_count +1):
#         for end in range(start+uniq_count, N+1):
#             my_gems = gems[start:end]
#             if len(set(my_gems)) == uniq_count and len(my_gems) < minimum:
#                 minimum = len(my_gems)
#                 answer[0] = start + 1
#                 answer[1] = end
#                 break
#     return answer







# [3, 7]
print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
# [1, 3]
print(solution(["AA", "AB", "AC", "AA", "AC"]))
# [1, 1]
print(solution(["XYZ", "XYZ", "XYZ"]))
# [1, 5]
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))