## 1번째 -> 성공, 하지만.. 400ms 뭔디
n = int(input())
c = list(map(int, input().split()))
print(min(c), max(c))

## 2번째 -> 런타임에러... ㅜ머지
n = int(input())
c = list(map(int, input().split())).sort()
print(c[0], c[-1])