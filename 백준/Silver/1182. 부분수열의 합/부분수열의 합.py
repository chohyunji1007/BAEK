from itertools import combinations #배열 모든 (조합)을 구해줌

n, s = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
for i in range(1, n+1):
    comb = combinations(arr, i) #배열, 원소개수

    for x in comb:
        if sum(x) == s:
            cnt += 1

print(cnt)