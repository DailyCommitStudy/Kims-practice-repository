# 앞 뒤 번호ㅔ에게만 빌릴 수 있다
# 여분을 가져온 학생이 도난 당했을 수도 있다
# 내가 좀 많이 독특하게 푼 편인듯..

def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()

    # 번호별 체육복 개수 체크 (0번, n+1번 인덱스 오류 방지)
    case = [0] + [1] * n + [0]
    for l in lost:
        case[l] -= 1
    for r in reserve:
        case[r] += 1

    # 잃어버린 사람들이 빌리는 것 체크
    for l in lost:
        if case[l] == 0 :
            if case[l - 1] > 1:
                case[l - 1] -= 1
                case[l] += 1

            elif case[l + 1] > 1:
                case[l + 1] -= 1
                case[l] += 1

    return n - case.count(0) + 2

print(solution(5, [4, 5], [3, 4]))

# 굳이 case 라는 리스트를 만들지 않고도 풀 수 있는 방법
