'''
생성 마법: 고양이 1마리 생성
복제 마법: 집에 있는 고양이 일부 또는 전부를 대상으로 복제 (k마리가 있다면, 0 ~ k 추가 가능)

위 2가지 마법을 사용해 최소의 행동 횟수로 정확히 N마리의 고양이가 있도록 하자.
이때 최소 행동 횟수는?

일단 어떻든 생성 마법을 하나는 써야함
N = 6
생성(1) -> 복제(2) -> 복제(4) -> 복제(6)

그러면 생성 후 복제를 반복하면서 k개씩 추가. 
N-k가 k보다 작을 경우 마지막 마법 하고 끝

만약 마법을 쓴 뒤 k == N일 경우?
'''



N = int(input())

answer = 0
k = 0

while N > k:
    if k == 0: # 고양이가 없을 경우, 생성
        k += 1
    else:      # 고양이 복제 (0마리 이상, k마리 이하 생성)
        k += k
    answer += 1

print(answer)