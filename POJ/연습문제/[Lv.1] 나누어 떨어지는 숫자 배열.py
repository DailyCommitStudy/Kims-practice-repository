# 단순한 문제..
# 스택,큐를 이용하는 문제고, 리스트에 넣을 때 divisor로 나눴을 때 나머지가 0인 경우를 필터링하고 정렬했다.

def solution(arr, divisor):
    answer = sorted([a for a in arr if a%divisor==0])
    return answer if answer else [-1]

# 다른 사람의 코드(1)
'''
나와 코드 자체는 같지만 or를 활용했다.
 굳이 조건문으로 비교하지 않아도 or을 사용하면 앞에 있는 값이 거짓일 때 뒤의 값까지 호출된다고.. ㄷㄷㄷ
 나름 비교할 때 answer만 넣는 것으로 논리적으로 생각했다고 생각했는데 ㅋㅋ
 이런 로직이 있따니.. 이렇게 또 하나 배워간다
'''
def solution(arr, divisor):
    return sorted([n for n in arr if n%divisor == 0]) or [-1]