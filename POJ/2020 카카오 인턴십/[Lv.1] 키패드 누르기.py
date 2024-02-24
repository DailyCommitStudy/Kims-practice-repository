'''
1 2 3
4 5 6
7 8 9
* 0 #
'''

# 1, 4, 7 -> L
# 3, 6, 9 -> R
# 2, 5, 8, 0 -> 가까운 손가락

# L, R 각 손가락이 마지막으로 누른 번호 저장
# 문제: 거리를 어떻게 계산할까?
# 거리: 얼만큼 이동해야 하는가. p[1][1] -> p[2][1] 2-1 + 1-1 = 1
# p[0][2] - p[1][1] = abs(0-2 + 1-1) = 2 이런식으로 계산..?
# 아니면 1차원 배열 [1,2,3,4,5,6,7,8,9,"*",0,"#"]로 했을 때는 계산할 수 없을까?
# 3(2) -> 5(4): (4 - 2)//3 + (4-2)%3 = 2
# 1(0) -> 0(10): (10)//3 + 10%3 = 3 + 1 = 4
# 0(11) -> 1(1):  -10//3

def solution(numbers, hand):
    L, R = 10, 12  # 손가락 위치 초기화 (*은 10번째, #은 12번째 수)
    h = {"right": "R", "left": "L"}
    pad = ['', 1, 2, 3, 4, 5, 6, 7, 8, 9, "*", 0, "#"]
    answer = ''

    for n in numbers:
        if n in [1, 4, 7]:   # 왼손
            answer += "L"
            L = n
        elif n in [3, 6, 9]: # 오른손
            answer += "R"
            R = n
        else:
            # 왼, 오 거리 차이 구하기
            m = pad.index(n) # 0일 수도 있으니 index()로 위치 구한 뒤 계산
            distance = (abs(L - m) // 3 + abs(L - m) % 3) - (abs(R - m) // 3 + abs(R - m) % 3)
            if distance == 0: # 거리가 같다 -> hand에 따라서 결정
                answer += h[hand]
                if answer[-1] == "L":
                    L = m
                else:
                    R = m

            elif distance > 0:  # 양수, 즉 오른손이 가깝다
                answer += "R"
                R = m

            else:  # 음수, 왼손이 가깝다
                answer += "L"
                L = m

    return answer

## 다른 사람의 풀이
# 나와 비슷하지만 이차원 배열로 푼 방법
def solution(numbers, hand):
    answer = ''
    key_dict = {1:(0,0),2:(0,1),3:(0,2),
                4:(1,0),5:(1,1),6:(1,2),
                7:(2,0),8:(2,1),9:(2,2),
                '*':(3,0),0:(3,1),'#':(3,2)}

    left = [1,4,7]
    right = [3,6,9]
    lhand = '*'
    rhand = '#'
    for i in numbers:
        if i in left:
            answer += 'L'
            lhand = i
        elif i in right:
            answer += 'R'
            rhand = i
        else:
            curPos = key_dict[i]
            lPos = key_dict[lhand]
            rPos = key_dict[rhand]
            ldist = abs(curPos[0]-lPos[0]) + abs(curPos[1]-lPos[1])
            rdist = abs(curPos[0]-rPos[0]) + abs(curPos[1]-rPos[1])

            if ldist < rdist:
                answer += 'L'
                lhand = i
            elif ldist > rdist:
                answer += 'R'
                rhand = i
            else:
                if hand == 'left':
                    answer += 'L'
                    lhand = i
                else:
                    answer += 'R'
                    rhand = i

    return answer