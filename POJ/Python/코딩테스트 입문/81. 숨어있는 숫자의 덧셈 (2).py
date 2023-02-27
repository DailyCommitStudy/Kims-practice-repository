def solution(my_string):
    i = 0
    answer = 0
    while i <= len(my_string) :
        for j in range(4,0,-1) :
            if my_string[i:i+j].isdigit() :
                answer += int(my_string[i:i+j])
                i += (j-1)
                break
        i += 1

    return answer

# 시도하려다 실패했는데 이러면 되는구나?
def solution(my_string):
    s = ''.join(i if i.isdigit() else ' ' for i in my_string)
    return sum(int(i) for i in s.split())