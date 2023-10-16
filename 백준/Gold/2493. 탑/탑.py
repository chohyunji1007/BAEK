from collections import deque
N = int(input().strip())
tower = list(map(int, input().strip().split()))
st = []
result = []
for i in range(N):
    while st and tower[st[-1]] < tower[i]:
        st.pop()
    if not st:
        result.append(0)
    else:
        result.append(st[-1] + 1)
    st.append(i)
print(*result)