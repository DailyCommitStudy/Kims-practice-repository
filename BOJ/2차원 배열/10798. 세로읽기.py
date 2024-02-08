# A ~ Z, a ~ z, 0 ~ 9
# 각 단어의 길이는 각각 다르다
# 각 입력을 2차원으로 받는다
# 세로로 읽을 때, try - except 문으로 index error가 뜨면 넘어가게

# 입력 받기
arr = [input() for _ in range(5)]

for j in range(15):
    for i in range(5):
        # 세로로 읽을 때, 해당 글자가 없을 때는 try-excpet 문으로 넘어가기
        try:
            print(arr[i][j], end='')
        except IndexError:
            continue