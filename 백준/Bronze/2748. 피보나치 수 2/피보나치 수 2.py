number = int(input())
f_arr=[]
def f(n):
    
    f_arr.append(0)
    f_arr.append(1)

    for i in range(2,n+1):
        f_arr.append(f_arr[i-1]+f_arr[i-2])

    return f_arr[n]

print(f(number))