a, b = map(int, input().strip().split(' '))

for i in range(b):
    print("*"*a)

# 다른 사람 코드
# 하 생각했던 방법인데 미친것..
# 근데 시간 복잡도는 그닥 다르지 않은 듯~
a, b = map(int, input().strip().split(' '))
answer = ('*'*a +'\n')*b
print(answer)
