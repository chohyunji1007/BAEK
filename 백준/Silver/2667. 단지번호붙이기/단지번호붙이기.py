n = int(input())
matrix =[]
for _ in range(n):
    matrix.append(list(input()))

dx =[-1,1,0,0]
dy =[0,0,-1,1]

visited=[[0]*n for _ in range(n)]
home_arr=[] 

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


home_group=0
for i in range(n):
    for j in range(n):
        if matrix[i][j]!='0' and visited[i][j]==0:
        
            home_count=0
            count_home(i,j)
            home_group+=1
            if home_count==0: #집이 1칸일때
                home_count=1
            home_arr.append(home_count)

home_arr.sort()
print(home_group)
for i in range(len(home_arr)):
    print(home_arr[i])  