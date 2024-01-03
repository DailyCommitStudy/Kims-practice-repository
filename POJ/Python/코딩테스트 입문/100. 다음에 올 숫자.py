# common의 각 원소 사이의 차이를 구한다
# 각 원소가 같으면 등차, 다르면 등비

def solution(common):
    diff = [common[i]-common[i-1] for i in range(len(common)-1, 0, -1)]
    if len(set(diff)) == 1: # 등차수열
        return common[-1] + diff[0]
    else: # 등비수열
        return common[-1] * common[1]//common[0]

### 다른 사람의 풀이
# 길이가 얼마나 길든 그 중 연속된 3개만 있어도 수열이다!!!
# 연속된 a, b, c가 있을 때 b-a, c-b로 등차인지 아닌지를 구하고 정답을 return한다
# 불필요한 계산없이 깔끔한 방법인듯 ㄷㄷ

def solution(common):
    answer = 0
    a,b,c = common[:3]
    if (b-a) == (c-b):
        return common[-1]+(b-a)
    else:
        return common[-1] * (b//a)
    return answer