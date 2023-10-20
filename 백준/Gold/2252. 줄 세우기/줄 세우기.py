import sys
from collections import deque

n, m= map(int,input().split())
# print(n, m)
# 다음 줄은 키를 비교한 두 학생의 번호 A, B > A가 학생B 앞에 
# 학생은 1~n번
# 학생들을 앞에서부터 줄 세운 결과

graph = [[] for _ in range(n+1)]
inDegree = [0 for _ in range(n+1)]
queue = deque()
answer = []

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    inDegree[b] += 1

for i in range(1, n+1):
    if inDegree[i] == 0:
        queue.append(i)

while queue:
    tmp = queue.pop()
    answer.append(tmp)
    for i in graph[tmp]:

        inDegree[i] -= 1
        if inDegree[i] == 0:
            queue.append(i)

print(*answer)