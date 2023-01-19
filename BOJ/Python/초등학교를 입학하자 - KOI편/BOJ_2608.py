## 왜 실패지..ㅠㅠ 아오~ 맞는 것 같은데

# V, L, D 한 번만
# I, X, C, M 연속해서 세 번만
# 만약 위 조건에 걸려서 못할 경우는 작은 수를 왼쪽에 두면서 표현하는 수밖에 없음.


# 235 -> CCXXXV
# 2493 -> MMCD'XC'III
# 만약, 그 수가 1~3이면 1이 들어가는 숫자로 커버 가능
# 그 수가 4라면 작은 수 - 큰 수 를 해줘야함. ex) 40이면, 10 50을 해줘야한다는 것
# 1~3 / 4 / 5 / 6~9?
# 90 -> 100 - 10 i = 10,

dic = {'I':1, 'V':5,'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
dic_r = dict(sorted(dict(zip(dic.values(), dic.keys())).items(), reverse=True))
# print(dic_r)
def f1(a) :
    res = 0
    flag = False
    for i in range(len(a)) :
        if flag :
            flag = False
            continue
        if i == (len(a)-1) :
            res += dic[a[i]]
            break
        if dic[a[i]] >= dic[a[i+1]] :
            res += dic[a[i]]
        else :
            res += dic[a[i + 1]] - dic[a[i]]
            flag = True

    return res

res = f1(input()) + f1(input())

print(res)

res_t = ''
i = 1000
a = 0
while (i>0) :
    a = res // i
    # print(res_t, i, a)
    if a < 4 : res_t += dic_r[i] * a
    elif a == 4 : res_t += (dic_r[i] + dic_r[i*5])
    elif a == 9 : res_t += (dic_r[i*10] + dic_r[i])
    else : res_t += dic_r[i*5]

    res %= i
    i //= 10

print(res_t, end='')
