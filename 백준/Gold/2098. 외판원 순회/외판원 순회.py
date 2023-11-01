import sys
input = sys.stdin.readline
N = int(input())
city = [[-1] * N for _ in range(N)]
dp = [[-1] * (1<<N) for _ in range(N)]  

for i in range(N):
    row = list(map(int, input().split()))
    for j in range(len(row)):
        city[i][j] = row[j]

def dfs(idx, visited):
    global dp
    global city
    #print(idx, visited)         #test
    if visited == (1<<N) - 1:
         return city[idx][0] if city[idx][0] != 0 else float('inf')

    if dp[idx][visited] != -1:
        return dp[idx][visited]

    ret = float('inf')
    for i in range(N):
        if (visited & (1<<i)) == 0 and city[idx][i] != 0:
            tmp = dfs(i, visited | (1<<i))
            if tmp != float('inf'):
                ret = min(ret, city[idx][i] + tmp)

    dp[idx][visited] = ret
    return ret

ans = dfs(0, 1)
print(ans)