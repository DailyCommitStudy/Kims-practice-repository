## 첫번째 시도 > 92ms? 정도
for n in range(int(input()), 0, -1) : print(n)

## 두번째 시도 > 시간을 줄이기 위해 다른 사람 코드 참고 > 60ms
print("\n".join(map(str, range(int(input()), 0, -1))))