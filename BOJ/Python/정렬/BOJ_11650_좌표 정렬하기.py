# 다 좋은데 시간ㅇ ㅣ너무 오래걸린다 -> 4400ms... 이것도 좀 해결할 방법을 찾아봐야할듯

case = sorted([tuple(map(int, input().split())) for _ in range(int(input()))],
                key = lambda x: [x[0], x[1]])

for i in case:
    print(i[0], i[1])