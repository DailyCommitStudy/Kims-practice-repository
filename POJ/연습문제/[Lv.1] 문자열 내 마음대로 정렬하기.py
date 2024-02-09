## 이전에 공부했던 lambda 활용 적용
# n번째 문자가 같을 경우 단어 자체를 사전순으로 정렬해야하기 때문에 정렬 조건을
# x[n]과 x로 설정했다.
def solution(strings, n):
    return sorted(strings, key=lambda x: (x[n], x))