import sys
#sys.setrecursionlimit(10**6)

n, m =map(int, input().split())
graph =[[] for _ in range(n+1)]
visited =[0]*(n+1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

count=0
def dfs(x):
    global count
    
    visited[x]=1
    for i in graph[x]:
        if visited[i]!=1:
            dfs(i)

for i in range(1,n+1) :
    if visited[i]!=1:
        dfs(i)
        count+=1

print(count)