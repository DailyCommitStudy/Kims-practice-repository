def solution(numlist, n):
    numlist.sort(reverse=True)
    numlist.sort(key=lambda x : abs(x-n))
    return numlist
    
    ## 다른 사람 풀이
    # return sorted(numlist,key = lambda x : (abs(x-n), n-x))