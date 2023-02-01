# 5명의 심판, 1-10점
# 최고점과 최저점을 제외한 점수의 합을 총점으로.
# 최고, 최저를 뺀 나머지 3명의 점수 중 최고, 최저의 차이가 4점 이상이면 KIN

for _ in range(int(input())) :
    score = sorted(map(int, input().split()))[1:4]
    if score[-1]-score[0] < 4 : print(sum(score))
    else : print("KIN")