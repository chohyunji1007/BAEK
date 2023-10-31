import sys
input = sys.stdin.readline
test_case = int(input())
for _ in range(test_case):
    n = int(input()) #동전 가지수
    n_list = list(map(int, input().split())) #동전 종류 리스트 오름차순으로 주어짐
    m = int(input()) #합계

    dp = [[0]*(m+1) for _ in range(n)]
    for k in range(0,n):
        dp[k][0]=1

    for i in range(0,n):
        for j in range(1,m+1):
            dp[i][j] = dp[i-1][j]
            if j-n_list[i]>=0:
                dp[i][j]+=dp[i][j-n_list[i]]
    print(dp[n-1][m])