# n : numbers의 길이
# n이 짝수면, 0, 2, 4, ... 짝수 인덱스만 반복
## n = 6, 0(1), 2(3), 4(5), 0, 2, 4, ... 9번째는? 9 // (6//2), 즉 세번째 짝수 인덱스. 2*(3-1)+1
## 2*(k//(n//2)-1)
# n이 홀수면, 0, 2, 4, .. 1, 3, 5, ... 짝수 인덱스 훑고 홀수 인덱스 훑기
##


# def solution(numbers, k):
#     n = len(numbers)
#     if len(numbers)%2==0 : return numbers[2*(k//(n//2))]
#     else : return numbers

# # k번째, numbers의 개수 n
# def solution(numbers, k):
#     numbers += numbers * 300
#     for i in range(0, k+2, 2) :
#         answer = numbers[i]
#     return answer

## 다른 사람 풀이 보고 푼 것..
# 이해가 안되네 미친...
# 역시 수학을 잘해야 하는구나.. 미친..^^ 현타가 오는군
def solution(numbers, k):
    if ((k * 2) - 1)  % len(numbers) == 0 :
        return len(numbers)
    return ((k * 2) - 1) % len(numbers)
