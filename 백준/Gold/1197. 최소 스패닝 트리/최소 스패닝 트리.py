v, e = map(int,input().split()) # v 정점 개수 e 간선 개수

"""1. root를 저장하는 vroot 배열 생성"""
vroot = [i for i in range(v+1)] #root( 연결 요소중 가장 작은 값 , 처음에는 자기 자신)를 저장하는 배열
elist=[] #간선을 저장할 배열

for _ in range(e):
    elist.append(list(map(int,input().split())))

"""2. elist(간선)를 가중치 기준으로 정렬"""
elist.sort(key=lambda x:x[2]) 

"""3. 간선들이 이은 두 정점을 find 함수를 통해 root(sRoot, eRoot)를 찾음"""
def find(x):
   # print('x=',x)
    #print('vroot[x]=',vroot[x])
    if x!=vroot[x]:
        vroot[x]=find(vroot[x])
    return vroot[x]
"""4. 두 root가 다르다면 큰 root값을 작은 root값으로 만들어 연결되게 해줌"""

answer=0
for s,e,w in elist:
    sroot=find(s)
    eroot=find(e)

    if sroot!=eroot:
        if sroot>eroot:
            vroot[sroot]=eroot
        else:
            vroot[eroot]=sroot
# """5. 가중치를 더함"""
        answer+=w

print(answer)