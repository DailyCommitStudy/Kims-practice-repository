A, B, C = map(int, input().split())
D = int(input())

s = (C+D)%60
m = (B + (C+D)//60)%60
h = (A+(B + (C+D)//60)//60)%24

print(h, m, s)