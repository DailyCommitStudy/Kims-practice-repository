case = input()

res = 10
for i in range(1, len(case)) :
    if case[i-1] == case[i] : res += 5
    else : res += 10

print(res)