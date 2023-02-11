## 내가 짠 코드
def solution(n):
    answer = n/7
    if answer == int(answer) : return answer
    else : return int(answer + 1)

## 천재들 코드.. 진짜 미친 거 아님? ㅜㅜㅜㅜ 미친 ㅜㅜㅜ
def solution(n):
    return (n - 1) // 7 + 1