import sys
input = sys.stdin.readline
t = int(input())
grade = []

for k in range(t):
    n = int(input())
    for i in range(n):
        grade.append(list(map(int, input().split())))

    gs = sorted(grade)

    cnt = 0
    min = gs[0][1]
    for i in range(n):
        if min >= gs[i][1]:
            cnt += 1
            min = gs[i][1]

    grade = []
    print(cnt)