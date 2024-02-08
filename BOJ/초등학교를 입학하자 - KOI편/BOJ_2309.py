hei = [int(input()) for _ in range(9)]
n_hei = hei.copy()
flag = False

for i in range(9) :
    for j in range(i+1, 9) :
        if (sum(hei) - hei[i] - hei[j]) == 100:
            n_hei.remove(hei[i])
            n_hei.remove(hei[j])

            flag = True
            break

    if flag : break

n_hei = sorted(n_hei)
for h in n_hei :
    print(h)