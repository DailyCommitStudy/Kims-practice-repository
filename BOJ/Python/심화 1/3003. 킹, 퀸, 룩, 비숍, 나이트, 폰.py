sett = [1, 1, 2, 2, 2, 8]

for i, a in enumerate(map(int, input().split())):
    print(sett[i]-a, end=" ")

# 한 개씩 가져오는 방법도 있지만,
# 만약 넘파이같은 브로드캐스팅이 가능한 라이브러리를 쓴다면 더욱 간편하게 가능할 것 같다.