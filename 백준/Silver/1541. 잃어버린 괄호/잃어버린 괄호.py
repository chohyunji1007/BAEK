get_str = list(input().split('-'))
# print(get_str)
arr=[]

for v in get_str:
    get_sum=0
    v = v.split('+')
    if len(v)>1:
        for get_v in v:
            get_sum+=int(get_v)
        arr.append(get_sum)
    else:
        arr.append(int(v[0]))


anw=0
for i in range(len(arr)):
    if i==0:
        anw=arr[i]
    else:
        anw-=arr[i]
print(anw)