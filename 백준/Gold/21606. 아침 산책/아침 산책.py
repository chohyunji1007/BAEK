from collections import deque
import sys
sys.setrecursionlimit(10**6)
n = int(input())
in_out=[]
in_out = list(map(int,input())) #인덱스 i-1 로 조회
graph=[[]*(n+1) for _ in range(n+1)]
how=[]
visited=[0]*(n+1)
# print(in_out)

for _ in range(n-1):
    a, b = list(map(int,input().split()))
    graph[a].append(b)
    graph[b].append(a)

# print('hi')

answer=[]
def dfs(x):
    global answer
    if visited[x]==0:
        visited[x]=1
        answer.append(x)
    
    for value in graph[x]:
        if visited[value]==0:
            answer.append(value)
            visited[value]=1
            if in_out[value-1]==1: #in_out이 1 인 경우 종료 
                how.append(answer)
                answer = answer[:-1]
            else: #in_out이 0 인 경우 계속
                dfs(value)

for i in range(1,n+1):
    answer=[]
    visited=[0]*(n+1)
    if in_out[i-1]!=0: #실외에서 시작 못함
        dfs(i)

print(len(how))