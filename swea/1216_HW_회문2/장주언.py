# 100x100의 글자판
# A, B, C 세 종류의 char type 단어가 입력되어있다.
# 그 중 직선으로만 회문 구조를 가지는 가장 긴 단어를 찾아라

# 노가다로 생각하면 -- - -- - -> [0]에서 [99]가 같으면 안으로 들어가서 [1]과 [98]이 같으면 .. 의 반복
# [0]과 [99]가 다르면 break, [1]과 [99]가 같다면...?
# 반대로 [0]과 [98]이 같다면?
# start 를 0과 99, 같지 않다면 0과 98, 1과 99를 비교 => 같다면 기존에서 index값을 +1, -1 각각 해주면서 비교
# 같다면 계속 진행, 다르다면 다시 밖으로 나와서 0과 97, 2와 99를 비교

# 이상한데??????????

# 다른 방식으로 표현하면
# 회문의 총 길이를 설정한 후 행을 슬라이스 해서 구해보자
# 총 길이가 100 일 경우는 한 다 맞으면 한행이 회문
# 총 길이가 99일 경우에는 0~98, 1~99를 확인하고
# 총 길이가 98일 경우에는 ...... 반복
# 계속해서 회문의 길이를 줄여가면서 회문이 나오면 Break 거는 식으로.
# 나오지 않으면 False처리후 다음 행으로 진행
# 가로, 세로 확인하기
# ㅠㅜㅠㅜㅠㅜㅠㅜㅜㅠㅜㅠㅜㅠㅜㅠㅜㅠㅜ




import sys

sys.stdin = open('./input.txt')

T = 10

for tc in range(1, T+1):
    input()
    # 글자판 letter board를 받아주고
    lb = [list(map(str, input().split())) for _ in range(100)]

    # 회문의 길이를 length라 할 때, 긴 길이의 회문부터 확인 할 것이므로 범위를 리버스
    for length in range(100, -1, -1):


        # 행은 0에서 99
        for row in range(100):
            # 열은 0에서 99 - length + 1

            for col in range(0, 100-length + 1):
                        # row,col 에서 부터 row, col+length-1의 값이 같다면?
                if lb[row][col] == lb[row][col+length-1]:
                            # 안의 내용들을 확인한다.

                    for idx in range(1, length//2):  # 짝홀수 관계없는 이유가 홀수이면, 중간값이 어떤 수가 와도 상관이 없다.
                        if lb[row][col+idx] == lb[row][col+length-1-idx]:
                                    count += 1

                        else:
                                reak
                else:
                    break




