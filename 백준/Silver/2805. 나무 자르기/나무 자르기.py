def binary_search(target, tree): #M ,arr, tree
    start = 0
    end = max(tree)+1

    while start <= end:
        mid = (start + end) // 2

        sum=0
        for tree_h in tree:
            if tree_h - mid>0:
                sum+=tree_h - mid
     

        if sum == M:
            return mid
        
        elif sum > M:
            start = mid + 1
        else:
            end = mid -1

    return end


N_M=input().split()
N, M=int(N_M[0]), int(N_M[1]) #N 나무수 M 가져가려는 나무 길이
t = input().split()
tree_a=[]
for i in range(N):
    tree_a.append(int(t[i]))


print(binary_search(M,tree_a))