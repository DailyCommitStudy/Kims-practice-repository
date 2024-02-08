# 문제에서 요구하는 것은 최대로 N/2개를 고를 수 있고,
# 중복되는 종류가 있을 때 최대 몇 종류의 포켓몬을 고를 수 있느냐.
# 그렇다면 nums를 set으로 바꿔 유니크한 값만 남도록 한 뒤, 그 개수를 센다.
# 그 개수가 N/2보다 크다면 N/2가 최대로 다양하게 고른 것이고
# N/2보다 작으면 유니크한 값의 개수가 최대로 다양하게 고른 것이다.

# 해시는 key-value.. 를 쓰는 건데 그냥 set을 쓴 거라 이게 맞나 싶긴 하다

def solution(nums):
    # N/2
    anslen = len(nums) // 2
    # 유니크한 값의 개수
    uniqlen = len(set(nums))
    # 유니크한 값의 개수가 N/2보다 크면 N/2 return
    if uniqlen > anslen:
        return anslen
    else:  # 아닌 경우 유니크한 값의 개수 return
        return uniqlen

# 다른 사람의 코드
# 걍 말이 안나온다 미친 난 왜 이걸 생각 못했을까 ㅋㅋㅋㅋㅋㅋㅋㅋㅋ 와 ㅁㅊ!!!!!
def solution(nums):
    return min(len(nums)/2, len(set(nums)))
