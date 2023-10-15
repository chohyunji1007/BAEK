import math
def is_prime(x): #소수구하기
    if x==1:
        return False

    for i in range(2, int(math.sqrt(x) + 1)):	# 2부터 x의 제곱근까지의 숫자
        if x%i == 0:		# 나눠떨어지는 숫자가 있으면 소수가 아님
            return False
    return True	
        

def fun(num):
    c, d= num//2, num//2
    while c>0:
        if c+d==num:
            if is_prime(c) and is_prime(d): #둘다 소수인 경우
                return print(c,d)
            
        c-=1
        d+=1
            

data_len = int(input())
arr=[]
arr2=[]
for i in range(0,data_len):
    arr.append(int(input()))
for j in range(0,len(arr)):
    fun(arr[j])