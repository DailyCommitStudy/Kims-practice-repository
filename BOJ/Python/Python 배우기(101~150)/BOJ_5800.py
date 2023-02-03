for t in range(int(input())) :
    score = sorted(list(map(int, input().split()))[1:], reverse=True)

    gap = score[0]-score[1]
    for i in range(1, len(score)-1):
        if gap < score[i]-score[i+1] : gap = score[i]-score[i+1]

    print("Class", t+1)
    print(f'Max {max(score)}, Min {min(score)}, Largest gap {gap}')