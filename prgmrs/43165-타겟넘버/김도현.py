

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


input_numbers = [1, 1, 1, 1, 1]
input_target = 3

# input_numbers = [4, 1, 2, 1]
# input_target = 4

print(solution(input_numbers, input_target))
