n, c= map(int,input().split()) #n 집 개수 c 공유기 개수
x =[]
for _ in range(n):
    x.append(int(input()))
x.sort()
#print('x=',x)
#거리 차의 합이 가장 큰거!

min_len = 1
max_len = x[-1] - x[0]
get_len = 0

while min_len<=max_len:
    cnt = 1 # 설치한 공유기 개수  
    establish = x[0] # 마지막 설치 위치(집 위치->집에만 설치 가능하니까)
    mid = (min_len+max_len)//2 # 공유기 사이의 최소 거리
    for i in range(1,n):
        if x[i]-establish>=mid:
            establish=x[i] # 그 다음 공유기 설치
            cnt+=1 # 설치한 공유 개수 증가
          
    if cnt<c: # 설치한 공유기 개수가 설치해야 되는 공유기 개수보다 작으면
        max_len=mid-1 # 공유기 사이의 거리를 축소
    elif cnt>=c: # 설치한 공유기 개수가 설치해야 되는 공유기 개수보다 크거나같으면
        min_len=mid+1 # 공유기 사이의 거리를 확대
        get_len=mid # result 갱신
    else:  # 설치한 공유기 개수와 설치해야되는 공유기 개수가 일치하면 
        get_len = mid 
        min_len=mid+1 # 가능한 거리의 최대값을 찾기위해 거리를 늘려가면서 계속 반복문 진행 
       
print(get_len)
