import sys
input = sys.stdin.readline
n, k = map(int,input().split()) #n 물품의 수 k 준서가 버틸 수 있는 무게
bag=[[0]*(k+1) for _ in range(n+1)]
bag_list=[]
for _ in range(n): 
    w, v = map(int, input().split()) #w 무게 v 가치
    bag_list.append([w,v])

for i in range(1,n+1):
    for j in range(1,k+1):
        if j>=bag_list[i-1][0]: #j가 현재 배낭 무게보다 큰 경우
            if bag[i-1][j-bag_list[i-1][0]]!=0: #0이 아니면!
                input_w = max(bag[i-1][j], bag[i-1][j-bag_list[i-1][0]]+bag_list[i-1][1])
                bag[i][j] = input_w
            else: #0이면
                bag[i][j]=max(bag_list[i-1][1], bag[i-1][j])
        else: #j가 현재 배낭 무게보다 작은 경우
            bag[i][j]=bag[i-1][j]
print(bag[n][k])