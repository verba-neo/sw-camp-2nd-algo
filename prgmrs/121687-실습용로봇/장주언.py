# G와 B는 현재 설정 된 방향에서 값을 이동
# R과 L로 방향을 설정하고 값을 이동하지는 않음

# direction을 설정해서 'G'와 'B'일 때 해당 direction을 통해 움직이게하려면

# G - > [0, 1] R 사용 후 G를 하면 -> [1, 1], L 사용 후 G를 하면 -> [1,2] R일 때 direction 값 +1 L일 때 -1 해주면서 4방향을 설정
# R,L에 따라 direction값을 더하거나 빼주면서 방향 설정 후 G와 B일때만 answer에 플러스 마이너스

def solution(command):

    answer = [0,0]
    # 방향전환에 따른 앞으로의 좌표이동 방향
    d_rows = [0, 1, 0, -1]
    d_col = [1, 0, -1, 0]
    # 첫 초기값 col에 +1 방향
    direction = 0

    for i in command:
        # 좌표이동
        if i == 'G':
            answer[0] += d_rows[direction]
            answer[1] += d_col[direction]
        # 좌표이동
        elif i == 'B':
            answer[0] -= d_rows[direction]
            answer[1] -= d_col[direction]
        # 방향전환
        elif i == 'R':
            direction = (direction + 1) % 4
        # 방향전환
        elif i == 'L':
            direction = (direction - 1) % 4

    return answer

# [2, 2]
print(solution('GRGLGRG'))

# [2, 0]
print(solution('GRGRGRB'))