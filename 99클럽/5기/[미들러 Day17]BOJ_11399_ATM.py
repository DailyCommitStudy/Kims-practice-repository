'''
소요시간이 작은 순으로 정렬
'''

N = int(input())
P = sorted(map(int, input().split()))

answer = sum([sum(P[:i]) for i in range(1, N+1)])

print(answer)