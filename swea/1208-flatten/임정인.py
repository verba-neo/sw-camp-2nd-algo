import sys
sys.stdin = open('./input.txt')

# 테스트 데이터 개수
T = 10

# 평탄화 시행 후 차이 최대 1 이내

for tc in range(1, T+1):
    N = int(input())  # 834
    numbers = list(map(int, input().split()))


    for i in range(N):
        max_n = max(numbers)
        min_n = min(numbers)
        idx_max_n = numbers.index(max_n)
        idx_min_n = numbers.index(min_n)
        numbers[idx_max_n] -= 1
        numbers[idx_min_n] += 1

        ans = max(numbers) -min(numbers)

    print(f'#{tc} {ans}')
