n, m = map(int, input().split())

maps = [[0]*(m+1) for _ in range(n+1)]
maps[0][0] = 1
for i in range(1, n+1):
    for j in range(1, m+1):
        maps[i][j] = (maps[i-1][j] + maps[i][j-1] + maps[i-1][j-1])% (int(1e9) + 7)
print(maps[n][m])