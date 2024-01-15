import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
n = int(input())
maps=[list(input().strip()) for _ in range(n)]

visited = [[False]*n for _ in range(n)]

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def dfs(x, y):
    visited[x][y]=True
    get_color = maps[x][y]
    for i in range(4):
        move_x, move_y = x+dx[i], y+dy[i]
        if -1<move_x<n and -1<move_y<n :
            if visited[move_x][move_y] == False and maps[move_x][move_y] == get_color:
                dfs(move_x, move_y)

count_N = 0
count_R = 0
for x in range(n):
    for y in range(n):
        if not visited[x][y]:
            dfs(x,y)
            count_N+=1

visited = [[False]*n for _ in range(n)]
for x in range(n):
    for y in range(n):
        if maps[x][y]=='G':
            maps[x][y]='R'

for x in range(n):
    for y in range(n):
        if not visited[x][y]:
            dfs(x,y)
            count_R+=1
print(count_N, count_R)