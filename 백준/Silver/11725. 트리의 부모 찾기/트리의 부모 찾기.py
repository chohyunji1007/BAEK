import sys
from collections import deque
sys.setrecursionlimit(10**6)
n = int(input()) #노드 개수

node_map = [[] for _ in range(n+1)]
p_node =[[] for _ in range(n+1)]
visited=[0] *(n+1)

for i in range(n-1):
    a, b = map(int, input().split())
    node_map[a].append(b)
    node_map[b].append(a)


def dfs(x):
    for i in node_map[x]:
        if visited[i]==0:
            visited[i]=x
            dfs(i)
        

dfs(1)
for j in range(2,n+1):
    print(visited[j])


# def bfs(x):
#     Q = deque()
#     Q.append(x)
#     while Q:
#         get_x = Q.popleft()
        
#         for value in node_map[get_x]:
#             if visited[value]==0:
#                 visited[value]=get_x        
#                 Q.append(value)
        
                
# bfs(1)
# for j in range(2,n+1):
#     print(visited[j])