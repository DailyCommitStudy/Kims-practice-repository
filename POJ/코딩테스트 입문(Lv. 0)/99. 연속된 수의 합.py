# total이 0부터 1000까지.
# num이 3이면 total이 0 되려면 -1 0 1.. 즉, -1부터 시작해야 함 (=-(3//2)
# 최대 범위는 total // num. 연속된 세 숫자여야하기 때문에

def solution(num, total):
    for i in range(-(num)//2, (total+1)//num):
        if sum(range(i, i+num)) == total:
            return list(range(i, i+num))

## 다른 사람의 풀이 (1)
# 솔직히 이해는 못하겠는데.. 해석에 따르면
'''
1. result를 일반화 시키면 [x+0, x+1, x+2, x+3 ... x + (num-1)]
2. 그리고 위 값을 전부 더한 값이 total이 됨. total = num*x + num*(num-1)//2 
    ※ result의 전체요소의 갯수는 num개 이므로 x의 갯수는 num개 이고 상수 부분은 첫번째 항이 0이고 
    마지막항이 num-1인 등차가 1인 등차수열의 합임.
3. 2번에서 도출한 공식을 이제 위 코드에 대입해보면 
    [(total - (num * (num - 1) // 2)) // num + i for i in range(num)] = [num*x + (num * (num - 1) // 2)) - (num * (num - 1) // 2)) // num + i for i in range(num)] = [num*x // num + i for i in range(num)] = [x + i for i in range(num)] 1번에서의 result x식과 일치하므로 정답이 됨.
'''

def solution(num, total):
    return [(total - (num * (num - 1) // 2)) // num + i for i in range(num)]

### 다른 사람의 풀이 (2)
# 수학적 패턴을 캐치할 수 있어야 이런 것도 보이나보다.. ㄷㄷ
# 아니면 등차수열의 원리를 내가 제대로 이해 못하고 있는 것 같다

def solution(num, total):
    answer = []
    var = sum(range(num+1))
    diff = total - var
    start_num = diff//num
    answer = [i+1+start_num for i in range(num)]
    return answer