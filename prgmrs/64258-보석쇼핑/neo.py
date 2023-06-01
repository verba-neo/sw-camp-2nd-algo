def solution(gems):
    N = minimum = len(gems)
    uniq_count = len(set(gems))
    answer = [1, N]
    for start in range(0, N-uniq_count+1):
        for end in range(start+uniq_count, N+1):
            my_gems = gems[start:end]
            if len(set(my_gems)) == uniq_count and len(my_gems) < minimum:
                minimum = len(my_gems)
                answer[0] = start + 1
                answer[1] = end
                break

    return answer


def solution(gems):
    start = 0
    N = minimum = len(gems)
    uniq_count = len(set(gems))
    answer = [1, N]
    # 구매 내역
    gem_info = {}

    for end in range(N):
        last_gem = gems[end]
        # 구매
        if last_gem in gem_info:
            gem_info[last_gem] += 1
        else:
            gem_info[last_gem] = 1

        # 모든 보석을 다 구매했다면,
        while uniq_count == len(gem_info):
            count = end - start + 1
            if count < minimum:
                minimum = count
                answer = [start+1, end+1]
            # 기존 구간의 첫번째 보석
            first_gem = gems[start]
            # 보석 개수 -1
            gem_info[first_gem] -= 1
            # 근데 보석 개수가 0이 되면
            if gem_info[first_gem] == 0:
                # K-V 삭제
                gem_info.pop(first_gem)
            # 구간 줄이기(Start 전진)
            start += 1

    return answer

# [3, 7]
print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
# [1, 3]
print(solution(["AA", "AB", "AC", "AA", "AC"]))
# [1, 1]
print(solution(["XYZ", "XYZ", "XYZ"]))
# [1, 5]
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))






















