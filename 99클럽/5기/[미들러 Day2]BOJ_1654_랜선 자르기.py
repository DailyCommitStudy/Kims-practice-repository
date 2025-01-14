k, n = map(int, input().split(' '))
lengths = [int(input()) for _ in range(k)]

# a = sum(lengths)//n   # 초기 길이 설정

# while True :
#     cnt = 0
#     for length in lengths:
#         cnt += length//a

#     if cnt >= n: break
#     else: a -= 1

# print(a)

# 어떻게 시간복잡도를 최적화할 수 있을지 모르겠다 ㅠㅠ -> chatGPT야 도와줘..
# chatGPT는 이진탐색을 써보래.. 뮤뭐라고..?
# 왜 이진탐색으로 풀 수 있는 걸까?
# 와 나는 왜 내가 최초로 짰던 코드가 -1 씩 배면서 직선 방향으로 탐색하는 코드라는 걸 왜 모르고 있었던 걸까
# 그 범위가 정해져 있는 건데 왜..?
# 이건 그냥 주어진 정수 범위 내에서 조건에 맞는 정수를 탐색하는 문제였던 거야..


low, high = 1, max(lengths)
result = 0

while low <= high:
    mid = (low + high) // 2
    cnt = sum(length // mid for length in lengths)
    
    if cnt >= n:
        result = mid  # 조건을 만족하므로 결과값 업데이트
        low = mid + 1  # 더 큰 길이를 탐색
    else:
        high = mid - 1  # 더 작은 길이를 탐색

print(result)