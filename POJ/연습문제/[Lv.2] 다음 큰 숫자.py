# 1의 갯수가 같다
# n을 이진수로 변환했을 때, 맨 뒤에서부터 가장 첫번째로 등장하는 1을 0으로 바꾸고, 그 다음으로 오는 0을 1로 바꾸면 될 것이다 => 아니넹
# 그냥 n부터 1씩 더해보면서 해보면 안됨? => 이게되네..
# 심지어 효율도 꽤좋음 ㅁㅊ..

def solution(n):
    i = 1
    while True:
        if bin(n).count("1") == bin(n+i).count("1"):
            return n+i
        i += 1


# 다른 사람 코드로 좀 더 디벨롭!
# 거의 같지만 디테일이 다름
def solution(n):
    cnt = bin(n).count("1")
    while True:
        n += 1
        if cnt == bin(n).count("1"):
            return n
