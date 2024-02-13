def solution(n):
    return (n**0.5+1)**2 if int(n**0.5) == n**0.5 else -1

## 다른 사람 코드
'''
와..
이게왜되지..
원리는 좀 더 검색해바야겄다..
'''
def nextSqure(n):
    return n == int(n**.5)**2 and int(n**.5+1)**2 or 'no'