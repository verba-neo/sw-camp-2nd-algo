import sys
sys.stdin = open('input.txt')

# 테스트 데이터 개수
T = int(input())

for tc in range(1, T+1):

    word, key = map(str, (input()).split())  # word, key 저장

    idx = 0
    count = 0

    while idx < len(word) - len(key) + 1:
        if word[idx:idx+len(key)] == key:
            count += 1
            idx += len(key)  # key 길이만큼은 이미 한 번으로 카운트 했으므로
        else:
            idx += 1

    # 결과 = 단어 길이 - 축약 단어 들어간 횟수*(축약 단어 - 1)
    result = len(word) - count*(len(key)-1)

    print(f'{tc} {result}')
