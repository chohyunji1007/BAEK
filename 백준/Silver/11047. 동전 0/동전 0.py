n, k= map(int,input().split()) #가진 동전 개수

coin_arr=[]
for _ in range(n):
    coin_arr.append(int(input()))

sum=0
count=0
for i in range(n-1,-1,-1):
    if coin_arr[i]<=k:
        head = k//coin_arr[i]
        # print(head)
        if head>=1:
            sum=coin_arr[i]*head
            # print(f'coin_arr[{i}]*head = {coin_arr[i]}*{head}')
            count+=head
            k-=sum
        if k==0:
            print(count)
            break