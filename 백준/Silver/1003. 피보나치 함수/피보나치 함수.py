# N이 주어졌을 때, fibonacci(N)을 호출했을 때, 0과 1이 각각 몇 번 출력되는지 구하는 프로그램
# 0이 출력되는 횟수와 1이 출력되는 횟수를 공백으로 구분해서 출력

t = int(input())
arr = [[1, 0], [0, 1]]
for _ in range(40):
    arr.append([0,0])

def get_count(n):

    if(n == 0):
        return arr[0]
    elif(n == 1):
        return arr[1]
    else:
        if arr[n]==[0,0]:
            arr[n]=[get_count(n-1)[0]+get_count(n-2)[0], get_count(n-1)[1]+get_count(n-2)[1]]
            return arr[n]
        else :
            return arr[n]

for _ in range(t):
    n = int(input())
    print(get_count(n)[0], get_count(n)[1])