#input = sys.stdin.readline
n, k = list(map(int,input().split())) #2n칸 컨테이너, 내구도 0인게 k개 이상인 경우 중단
a = list(map(int, input().split())) # 1, 2,,n,, 2n까지의 내구도

visited = [False for _ in range(n)]
def move():
    last = a.pop()
    a.insert(0,last)
    visited_last = visited.pop()
    visited.insert(0, visited_last)
    visited[n-1]=False

def fun():
    i = 1
    while 1:
        #1. 컨테이너, 현재 위치 회전
        move()

        #2. 로봇 한칸 이동
        for j in range(n-2,-1,-1):
            if visited[j] and not visited[j+1] and a[j+1]>0: #true이면 위에 로봇이 있는거
                a[j+1]-=1
                visited[j+1]=True
                visited[j]=False
        visited[n-1] = False
        #3. 로봇 0번 자리에 올리기
        if a[0]>0:
            a[0]-=1
            visited[0]=True
        check_count = a.count(0)
        if a.count(0)>=k:
            return print(i)
        i+=1
fun()  