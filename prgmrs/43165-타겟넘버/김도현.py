

def solution(number, target):

    answer = 0

    def dfs(tmp_sum, idx):
        nonlocal answer
        if tmp_sum == target and len(number)-1 == idx:
            answer += 1
            return
        elif len(number)-1 == idx:
            return
        dfs(tmp_sum+number[idx+1], idx+1)
        dfs(tmp_sum-number[idx+1], idx+1)

    dfs(number[0], 0)
    dfs(-number[0], 0)

    return answer


# 5
print(solution([1, 1, 1, 1, 1], 3))
# 2
print(solution([4, 1, 2, 1], 4))
