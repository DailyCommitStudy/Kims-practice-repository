# 한 번에 1, 2칸 뛰기 가능
# 피보나치수열.. 이 아닌가? 싶었는데 이전에 피보나치 수열 풀 떄 오버플로우 되는 걸
# 막기 위해 큰 수의 나머지로 해준 게 생각나서 해봤는데 이게 되네.. 뭐야이게 ㅁㅊ

def solution(n):
    answer, tmp = 1, 1
    if n <= 2:
        answer = n
    else:
        for i in range(1, n):
            answer, tmp = answer + tmp, answer

    return answer % 1234567