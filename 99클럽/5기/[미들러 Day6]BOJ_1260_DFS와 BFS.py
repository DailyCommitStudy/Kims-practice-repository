'''
입력:
정점의 개수 N(1~N번), 간선의 개수 M, 정점의 번호 V
간선(양방향)이 연결하는 두 정점의 번호
.
.
더이상 방문할 수 있는 점이 없는 경우 종료
'''

# # edge 추가
# def add_edge(graph, u, v):
#     if u not in graph:
#         graph[u] = []
#     if v not in graph:
#         graph[v] = []
#     graph[u].append(v)  # u -> v
#     graph[v].append(u)  # v -> u (양방향)


# 스택으로 DFS 탐색
def dfs(graph, start):
    visited = []
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            print(node, end=' ')
            # 스택은 리스트의 맨 뒷 값을 가져오며 탐색하기에 작은 노드부터 탐색하기 위해 내림차순으로 정렬한다
            stack += sorted(graph[node], reverse=True) 


# 큐로 BFS 탐색
def bfs(graph, start):
    visited = []
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            print(node, end=' ')
            queue += sorted(graph[node])


N, M, V = map(int, input().split(' '))

graph = {n:[] for n in range(1, N+1)}
for _ in range(M):
    u, v = map(int, input().split(' '))
    graph[u].append(v)  # u -> v
    graph[v].append(u)  # v -> u (양방향)

dfs(graph, V)
print()
bfs(graph, V)