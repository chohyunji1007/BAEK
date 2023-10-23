from collections import deque
n, m, k, x= map(int,input().split()) #n 도시개수 m 도로개수 k 거리정보 x 출발도시

graph = [[] for _ in range(n+1)]
distance = [0] * (n+1)
visited = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b) #방향이 있는 그래프

def bfs(start):
    answer=[]
    Q = deque()
    Q.append(start)
    visited[start]=1
    distance[start]=0

    while Q:
        get_start = Q.popleft()
        for i in graph[get_start]:
            if visited[i]==0:
                visited[i]=1
                Q.append(i)
                distance[i] = distance[get_start]+1

                if distance[i]==k:
                    answer.append(i)

    if len(answer)==0:
        print(-1)

    else:
        answer.sort()
        
        for i in answer:
            print(i, end='\n')
bfs(x)  
