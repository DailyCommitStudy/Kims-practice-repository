def solution(score):
    n_score = [(x[0]+x[1])/2 for x in score]
    sorted_score = sorted(n_score, reverse=True)

    return list(map(lambda x : sorted_score.index(x)+1, n_score))

# 다른 사람의 풀이(더 좋은 예)
# def solution(score):
#     a = sorted([sum(x) for x in score], reverse=True)
#     return [a.index(sum(x))+1 for x in score]