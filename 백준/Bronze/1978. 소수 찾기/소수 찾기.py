import math
def primenumber(x):
    if x==1:
        return False
    for i in range(2, int(math.sqrt(x) + 1)):	# 2부터 x의 제곱근까지의 숫자
        if x%i == 0:		# 나눠떨어지는 숫자가 있으면 소수가 아님
            return False
    return True
A, B=input(), input().split()
count=0
for i in range(len(B)):
    if primenumber(int(B[i]))==True:
        count+=1
print(count)