import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    dump_count = int(input())
    heights = list(map(int, input().split()))

    answer = 0
    boxes = []
    for r in range(len(heights)):
        one_line_boxes = []
        for c in range(heights[r]):
            one_line_boxes.append(0)
        boxes.append(one_line_boxes)

    for count in range(dump_count+1):
        longest_boxes_idx = 0
        shortest_boxes_idx = 0
        for idx, one_line_boxes in enumerate(boxes):
            if len(one_line_boxes) > len(boxes[longest_boxes_idx]):
                longest_boxes_idx = idx
            if len(one_line_boxes) < len(boxes[shortest_boxes_idx]):
                shortest_boxes_idx = idx

        if count == dump_count:
            answer = len(boxes[longest_boxes_idx]) - len(boxes[shortest_boxes_idx])

        boxes[longest_boxes_idx].pop()
        boxes[shortest_boxes_idx].append(0)

    print(f'#{tc} {answer}')
