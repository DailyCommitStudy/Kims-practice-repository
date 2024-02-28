# 이진 변환 횟수, 제거된 0의 개수
# 0 개수 카운드
def solution(s):
    answer = [0, 0]
    while s != "1":
        answer[1] += s.count("0")
        s = bin(len(s.replace("0", "")))[2:]

        answer[0] += 1

    return answer