arr=[]
data_len = int(input())
for i in range(0,data_len):
    arr.append(int(input()))
arr.sort()
for j in range(0,len(arr)):
    print(arr[j])