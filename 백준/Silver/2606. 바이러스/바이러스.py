n = int(input()) #컴퓨터 수
v = int(input()) #네트워크상 연결되어있는 컴퓨터 쌍의 수

graph = [[] for i in range(n+1)] # 그래프 초기화
visited=[0]*(n+1) #방문한곳 표시

for i in range(v): # 그래프 생성 #인덱스 : 컴퓨터 번호, 값: 연결된 컴퓨터 리스트
    a,b=map(int,input().split())
    graph[a]+=[b] # a에 b 연결
    graph[b]+=[a] # b에 a 연결 -> 양방향
    
def dfs(v):
    visited[v]=1
    for x in graph[v]:
        if visited[x]==0:
            dfs(x)
dfs(1)
print(sum(visited)-1)