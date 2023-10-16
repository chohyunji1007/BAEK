from collections import deque

# print(input().split())
input=input().split()
queue=deque([])
N=int(input[0])
K=int(input[1])
arr=[]
for i in range(0,N):
    queue.append(i+1)
# print('queue=',queue)
while len(queue)!=1:
    for j in range(0,K):
        if j!=K-1:
            out = queue.popleft()
            # print('out=',out)
            queue.append(out)
            
        else:
            in_arr=queue.popleft()
            # print('in_arr=',in_arr)
            arr.append(str(in_arr))
arr.append(str(queue.popleft()))
str='<'+', '.join(arr)+'>'
print(str)