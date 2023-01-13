# A, B, C = 5m=5*60s=300s, 1m=60s, 10s
T = int(input())

A, T = T//300, T%300
B, T = T//60, T%60
C = T//10

if T%10 != 0 : print(-1)
else : print(A, B, C)
