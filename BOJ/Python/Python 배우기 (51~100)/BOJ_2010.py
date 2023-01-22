## input() 함수가 비교적 느려서 readline을 써줘야 해결됨
import sys
n = int(input())
print(sum([int(sys.stdin.readline()) for _ in range(n)]) - (n-1))