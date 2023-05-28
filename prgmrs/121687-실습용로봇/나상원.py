def solution(command):
    answer = []

    x = y = 0
    direction = 0
    # 아래 오른 왼 위
    dxy = [[1, 0], [0, 1], [0, -1], [-1, 0]]

    for char in command:
        if char == 'R':
            direction = (direction+1) % 4
        elif char == 'L':
            direction = (direction-1) % 4
        elif char == 'G':
            x = x + dxy[direction][0]
            y = y + dxy[direction][1]
        elif char == 'B':
            x = x - dxy[direction][0]
            y = y - dxy[direction][1]

    answer.append(x)
    answer.append(y)

    return answer


print(solution('GRGLGRG'))
