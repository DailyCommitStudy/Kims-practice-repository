def solution(quiz):
    answer = []
    for q in quiz :
        q = '=='.join(q.split('='))
        # 아맞다 replace
        q = q.replace('=', '==')
        if eval(q) : answer.append("O")
        else : answer.append("X")
    return answer

