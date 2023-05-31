from itertools import combinations


# 조합으로 풀기
def solution(numbers, target):
    answer = 0
    # 4 C nc
    for negative_count in range(len(numbers)+1):
        for case in combinations(range(len(numbers)), negative_count):
            copy_numbers = numbers[:]
            for idx in case:
                copy_numbers[idx] *= -1

            if sum(copy_numbers) == target:
                answer += 1
    return answer


# DFS(상태공간트리)로 풀기
def solution(numbers, target):
    answer = 0

    def dfs(idx, num):
        nonlocal answer

        if idx == len(numbers):
            if num == target:
                answer += 1
        else:
            dfs(idx+1, num + numbers[idx])
            dfs(idx+1, num - numbers[idx])

    dfs(0, 0)
    return answer


# 5
print(solution([1, 1, 1, 1, 1], 3))
# 2
print(solution([4, 1, 2, 1], 4))

