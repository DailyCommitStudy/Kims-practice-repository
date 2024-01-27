# 1) 단순하게 enter면 리스트에 추가, 그게 아니면 퇴근 (리스트에서 삭제)
# -> 시간초과 -> enter 를 set으로 바꿔주기
# -> 43313KB / 4020ms 성공

res = []
enter = set()

for _ in range(int(input())):
    name, state = input().split()
    if state == "enter" : enter.add(name)
    else : enter.remove(name)

enter = sorted(list(enter), reverse=True)
for i in enter : print(i)