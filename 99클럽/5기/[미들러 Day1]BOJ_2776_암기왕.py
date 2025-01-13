for _ in range(int(input())):
    N = int(input())
    # 순서가 중요하지 않으니 set으로 저장
    note1 = set(map(int, input().split(' ')))

    M = int(input())
    note2 = list(map(int, input().split(' ')))

    for n in note2:
        if n in note1: print(1)
        else: print(0)