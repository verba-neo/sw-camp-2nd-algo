

def solution(number, target):

    answer = 0
    stack = []
    idx = 0
    stack.append(number[idx])
    stack.append(-number[idx])
    num_len = len(number)

    while stack:
        tmp = stack.pop(0)
    return


# 5
print(solution([1, 1, 1, 1, 1], 3))
# 2
print(solution([4, 1, 2, 1], 4))
