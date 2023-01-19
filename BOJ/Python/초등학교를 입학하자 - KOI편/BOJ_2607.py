# 같은 종류의 문자로 이루어짐
# 같은 문자는 같은 개수 만큼 있다
# 같은 구성 -> 비슷한 단어
# DOG, GOD -> 같은 구성, 비슷한 단어
# GOD, GOOD -> 비슷한 단어
# DOG, DOLL은 비슷한 단어 X

n = int(input())

a = input()
res = 0
# print(a)

for _ in range(n-1) :
    b = input()
    c = dict()
    check = 0   # 비슷한 단어인지 아닌지
    # print(b)
    for aa in a :
        if aa not in b :
            check += 1
        elif aa in c :
            c[aa] += 1
            if c[aa] > b.count(aa) + 1 : check += 2
        else : c[aa] = 1
        # print(bb, c, a.count(bb))
    if check < 2 : res += 1

print(res)