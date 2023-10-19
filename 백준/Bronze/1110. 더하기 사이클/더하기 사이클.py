n=int(input())
if n<10:
    n=str(n).zfill(2)


def fun(x,y):
    return y*10+(x+y)%10

n=int(n)
a=n//10
b=n%10
count=1
while True:
    # print(a, b)
    if fun(a,b)==n:
       print(count)
       break
    else:
        
        count+=1
        x=b
        y=(a+b)%10
        a, b = x, y
        fun(a,b) 