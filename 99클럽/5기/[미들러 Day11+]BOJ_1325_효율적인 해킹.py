'''
# 한 번의 해킹으로 여러 컴퓨터를 해킹할 수 있는 컴퓨터를 해킹하자 !!
# 컴퓨터의 신뢰하는 관계와 신뢰하지 않는 관계
# A->B B를 해킹하면 A도 해킹 가능

# 연결 리스트.. 로 저장하면 안되나?

# 5 4 = 5는 4를 신뢰한다 -> 4 해킹 시 5도 해킹 가능

5 4
3 1
3 2
4 3
5 3

5 <- 4
3 <- 1
3 <- 2
4 <- 3
5 <- 3

4, 5 <- 3 <- 1, 2

그래프같은데.
그래프로 저장해서 탐색하고, 간선별로 개수를 카운트한 뒤에 최대값을 가진 노드만 오름차순 출력?
DFS를 써야할 것 같음
방향성이 있는 그래프 !!

파이썬은 쉽지 않다네요..
극단적인 문제..ㅜㅜ
'''

def dfs(graph, node, visited):
    if node in visited:
        return 0

    visited.add(node)
    count = 1  # 자기 자신 포함

    for neighbor in graph[node]:
        count += dfs(graph, neighbor, visited)  # 탐색한 노드 수 추가

    return count


N, M = map(int, input().split(' '))
graph = {n:[] for n in range(1, N+1)} # 컴퓨터는 1번부터 N번까지 존재

for _ in range(M):
    a, b = map(int, input().split(' '))
    graph[b].append(a)  # a가 b를 신뢰, b에서 a에 접근 가능

# 해킹 가능한 컴퓨터 개수 카운트
cnt = [[n, 0] for n in range(1, N+1)]

for n in range(1, N+1):
    visited = set()  # 방문한 노드를 저장할 집합
    cnt = dfs(graph, n, visited)  # 1번 노드에서 시작

    cnt[n-1][1] = cnt

cnt.sort(key=lambda x: x[1], reverse=True) # 해킹할 컴퓨터가 많은 순으로 정렬
m = cnt[0][1]
for k, v in cnt:
    if m > v: break
    print(k, end=' ')