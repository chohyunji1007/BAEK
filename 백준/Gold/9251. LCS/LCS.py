str1= list(map(str, input()))
str2 = list(map(str, input()))
str1.insert(0,'*')
str2.insert(0,'*')

max_len=0
matrix = [[0]*(len(str2)+1) for _ in range(len(str1)+1)]
result = 0 
for i in range(1,len(str1)):
    for j in range(1,len(str2)):
        if str1[i]==str2[j]:
            matrix[i][j] = matrix[i-1][j-1]+1
        else:
	        matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])
        if result<matrix[i][j]:
            result = matrix[i][j]
print(result)