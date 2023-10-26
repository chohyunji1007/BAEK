n = int(input())
matrix =[]
for _ in range(n):
    matrix.append(list(input()))

dx =[-1,1,0,0]
dy =[0,0,-1,1]

visited=[[0]*n for _ in range(n)]
count_h=[] 

home_count=0
def count_home(x,y):
    global home_count
    for i in range(4):
        new_x = x+dx[i]
        new_y = y+dy[i]
        if 0<=new_x<n and 0<=new_y<n:
            if matrix[new_x][new_y]!='0':
                if visited[new_x][new_y]==0: #방문 안한곳
                    visited[new_x][new_y]=1
                    home_count+=1
                    count_home(new_x,new_y)


ice_count=0
for i in range(n):
    for j in range(n):
        if matrix[i][j]!='0' and visited[i][j]==0:
        
            home_count=0
            count_home(i,j)
            ice_count+=1
            if home_count==0:
                home_count=1
            count_h.append(home_count)

count_h.sort()
print(ice_count)
for i in range(len(count_h)):
    print(count_h[i])  
