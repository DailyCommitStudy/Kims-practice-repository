# 소거법으로 들어가있지 않으면 삭제?
# 혹은 들어가 있으면 1차 채택?

# 키워드 포함 개수를 세서 모두 0이거나 2개 이상인 게 있으면 0...
# 하 효과적인 게 안떠올라ㅏㅏㅏㅏㅏㅏ

def solution(babbling):
    key = ["aya", "ye", "woo", "ma"]

    answer = 0
    for b in babbling :
        for k in key:
            print(b.count(k))

        print()

    # for b in babbling:
    #     print(b)
    #     for k in key:
    #         if k in b: b = ''.join(b.split(k))
    #         print(k,b)
    #     if b == '':
    #         answer += 1
    #         print("correct")
    #     print()

    return answer

print(solution(["aya", "yee", "u", "maa", "wyeoo", "woowoowoayaoaya"]))