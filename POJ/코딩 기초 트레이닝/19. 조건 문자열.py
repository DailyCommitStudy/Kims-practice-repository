def solution(ineq, eq, n, m):
    if eq == "!":
        if ineq == ">": return 1 if n>m else 0
        else: return 1 if n<m else 0
    else:
        if ineq == ">": return 1 if n>=m else 0
        else: return 1 if n<=m else 0


# 다른 사람 풀이
# 이런 방법도 있구나 이게 훨 깔끔한 것 같다
def solution(ineq, eq, n, m):
    answer = 0
    if n > m and ineq ==">":
        answer = 1
    elif n < m and ineq == "<":
        answer = 1
    elif n == m and eq == "=":
        answer = 1

    return answer