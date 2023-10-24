from collections import deque
n = int(input()) #1부터 n-1까지 기본 부품이나 중간 부품의 번호
#n은 완제품 번호
m = int(input()) #이밑으로 M개의 줄에 필요한 부품들 간의 관계가 x, y, k로 주어짐
#x, y, k = 중간부품이나 완제품 x를 만드는데 중간부품 or 기본부품 y가 k개 필요하다
matrix = [[] *(n+1) for _ in range(n+1)]
needs = [[0]*(n+1) for _ in range(n+1)] #개수 저장해서 넘기기

Q = deque()
degree = [0]*(n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    matrix[b].append((a,c))
    degree[a]+=1

for i in range(1, n+1):
    if degree[i]==0:
        Q.append(i)

while Q:
    now = Q.popleft()

    for next, next_need in matrix[now]:
        if needs[now].count(0) == n+1:
            needs[next][now] +=next_need

        else:
            for i in range(1, n+1):
                needs[next][i]+=needs[now][i]*next_need
        degree[next]-=1
        if degree[next]==0:
            Q.append(next)
    
for x in enumerate(needs[n]):
    if x[1]>0:
        print(*x)