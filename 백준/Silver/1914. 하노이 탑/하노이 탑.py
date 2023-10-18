def hanoi_f(x, y, n):
    if n == 1:
        print(x,y)
        return

    hanoi_f(x, 6-x-y, n-1) #1단계 (1->2)
    print(x, y) #2단계 (마지막원반 1->3)
    hanoi_f(6-x-y, y, n-1) #3단계 (2->3)

#메인
n = int(input())
print(2**n-1)
if n <= 20:
    hanoi_f(1,3,n)