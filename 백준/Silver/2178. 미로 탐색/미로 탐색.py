import sys
from collections import deque

n, m= map(int,input().split())
matrix = [list(map(int, input().strip())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
Q = deque()

dx=[-1,1,0,0] 
dy=[0,0,-1,1]

def next(x, y):
    
    Q.append((x,y))
    
    while Q:
        # print(Q)
        x,y =Q.popleft()
        for i in range(4): #상하좌우 확인
            

            new_x=x+dx[i]
            new_y=y+dy[i]
            if 0<=new_x<n and 0<=new_y<m:
                
                if visited[new_x][new_y]==0 and matrix[new_x][new_y]==1 :
                    visited[new_x][new_y]=1
                    Q.append((new_x,new_y))
                    matrix[new_x][new_y]=matrix[x][y]+1
    return matrix[n-1][m-1]             

print(next(0,0))