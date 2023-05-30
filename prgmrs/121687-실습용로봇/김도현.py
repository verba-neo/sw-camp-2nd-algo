

def solution(command):
    d_x = [0, 1, 0, -1]
    d_y = [1, 0, -1, 0]
    direction = 0
    location = [0, 0]

    for c in command:
        if c == "G":
            location[0] += d_x[direction]
            location[1] += d_y[direction]
        elif c == 'R':
            direction = (direction + 1) % 4
        elif c == 'L':
            direction = (direction - 1) % 4
        elif c == "B":
            location[0] -= d_x[direction]
            location[1] -= d_y[direction]
        print(c, direction, location)

    return location


input_command = "GRGLGRG"
# input_command = "GRGRGRB"
print(solution(input_command))
