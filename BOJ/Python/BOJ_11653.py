N = int(input())
for i in range(2, N+1) :
    while (N/i == N//i) :
        N = N//i
        print(i)