import copy
import sys

n,w = map(int,sys.stdin.readline().split())
dp = [[0 for _ in range(w+1)]for _ in range(n+1)]

for i in range(1,n+1):
    weight, cost = map(int,sys.stdin.readline().split())
    if i == 1: 
        if weight>w: 
            continue
        else:
            for j in range(weight,w+1): 
                dp[i][j] = cost
    else:
        if weight>w: 
            dp[i] = copy.deepcopy(dp[i-1])
        else:
            for j in range(1,w+1):
                if weight > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i-1][j], cost + dp[i-1][j-weight])
print(dp[n][w]) 