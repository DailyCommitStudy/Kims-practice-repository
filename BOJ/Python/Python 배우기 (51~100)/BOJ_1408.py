# sh, sm, ss = map(int, input().split(':'))
# eh, em, es = map(int, input().split(':'))
#
# res = sh * 60 * 60 + sm * 60 + ss - (eh * 60 * 60 + em * 60 + es)
res = 100
resh = res%60%60
resm = (res - resh*60*60)%60
ress = (res-resm*60)%60
print(ress//60//60, ress//60, ress)