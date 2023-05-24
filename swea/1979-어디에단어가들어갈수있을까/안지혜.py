import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())

    boxes = [list(map(int, input().split())) for _ in range(N)]
    vertical_boxes = [[] for _ in range(N)]
    for el in boxes:
        for idx, i in enumerate(el):
            vertical_boxes[idx].append(i)

    count = 0

    def check(boxes, r, c, count):

        for i in range(K):
            if boxes[r][c + i] != 1:
                break

            # if it's first loop
            # check if prev number is 1
            if i == 0 and c != 0:
                if boxes[r][c + i - 1] == 1:
                    break

            # if it's last loop
            # check last col => count up
            if i == K - 1:
                if c == N - K:
                    count += 1
                # check that next number is 1
                else:
                    if boxes[r][c + i + 1] == 1:
                        break
                    else:
                        count += 1

        return count


    for r in range(N):
        for c in range(N-K+1):

            # check that value is 1
            # check boxes
            if boxes[r][c] == 1:
                new_count = check(boxes, r, c, count)
                count = new_count

            # check vertical_boxes
            if vertical_boxes[r][c] == 1:
                new_count = check(vertical_boxes, r, c, count)
                count = new_count

    answer = count

    print(f'#{tc} {answer}')
