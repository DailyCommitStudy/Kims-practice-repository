# 못 품 -> 0
# 총 점수: 가장 높은 점수 5개의 합
# 각 문제에 대한 점수 0 <= 점수 <= 150

## 리스트 혹은 튜플을 통해 2차원으로 저장. 하나의 변수에 인덱스 점수 모두 저장
## 점수, 정렬된 점수

# score = sorted([(i, int(input())) for i in range(1,9)],
#                reverse=True,
#                key=lambda x: x[1])

## 1번째 방법 >> 점수와 정렬된 점수 리스트 활용 >> 76ms
# score = [int(input()) for i in range(8)]
# score_r = sorted(score, reverse=True)[:5]
# quiz = sorted([score.index(i)+1 for i in score_r])
#
# print(sum(score_r))
# for i in quiz : print(i, end=' ')

## 2번째 방법 >> 딕셔너리(점수:번호) >> 44ms
score = dict(sorted({int(input()):i for i in range(1,9)}.items(),
               reverse=True))
print(sum(list(score.keys())[:5]))
quiz = sorted(list(score.values())[:5])
for i in quiz : print(i, end=' ')

