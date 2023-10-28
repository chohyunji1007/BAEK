n= int(input())
data=[]
for _ in range(n):
    start_time , end_time = map(int,input().split())
    data.append([start_time, end_time])

data.sort(key=lambda x:(x[1],x[0]))

get_end_time = data[0][1] #제일 먼저 끝나는거 종료시간
count=1
for i in range(1,n):    
    if data[i][0]>=get_end_time:
        if data[i][0]==data[i][1]:
            count+=1
        else:
            get_end_time = data[i][1]
            count+=1
print(count)