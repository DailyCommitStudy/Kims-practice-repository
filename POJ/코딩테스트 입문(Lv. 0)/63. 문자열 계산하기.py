def solution(my_string):
    case = my_string.split(' ')
    answer = int(case[0])
    for i in range(1, len(case)-1, 2) :
        if case[i] == '+' : answer += int(case[i+1])
        else : answer -= int(case[i+1])
    return answer