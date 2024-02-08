for _ in range(int(input())) :
    a = list(filter(lambda x : x%2==0, map(int, input().split())))
    print(sum(a), min(a))