# 전공평점 = 전공과목별 학점 * 과목평점의 합을 학점의 총합으로 나눈다
# P인 과목은 계산에서 제외

# 평점
rate = {"A+":4.5, "A0":4.0, "B+":3.5, "B0":3.0, "C+":2.5, "C0":2.0, "D+":1.5, "D0":1.0, "F":0.0}
# 이수학점, 총성적
grades, credits = 0, 0

for _ in range(20):
    name, credit, grade = input().split()
    if grade == "P" : continue
    grades += float(credit) * rate[grade]
    credits += float(credit)

print(round(grades / credits, 6))


