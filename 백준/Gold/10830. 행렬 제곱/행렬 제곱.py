import sys

MOD = 1000

def multiply_matrix(A, B, N):
    result = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += A[i][k] * B[k][j]
            result[i][j] %= MOD
    return result

def matrix_power(A, B, N):
    if B == 1:
        return [[A[i][j] % MOD for j in range(N)] for i in range(N)]
    elif B % 2:
        temp = matrix_power(A, B-1, N)
        return multiply_matrix(A, temp, N)
    else:
        temp = matrix_power(A, B // 2, N)
        return multiply_matrix(temp, temp, N)

N, B = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

result = matrix_power(matrix, B, N)
for row in result:
    print(*row)

#10830