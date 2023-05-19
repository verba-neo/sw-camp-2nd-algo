# input.txt  파일을 한줄씩 (stdin) 입력 (open)
import sys
sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    print(tc, n)