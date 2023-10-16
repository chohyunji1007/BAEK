arr=[]
for i in range(0,9):
    arr.append(int(input()))
total_sum=sum(arr)
diff=total_sum-100
#print('arr=',arr)
def fun(num):
    for i in range(0,9):
        for j in range(0,9):
            if i!=j:
                if arr[i]+arr[j]==diff:
                    f=arr[i]
                    s=arr[j]
                    arr.remove(f)
                    arr.remove(s)
                    return 
                    

fun(input)
print(*sorted(arr),sep='\n')