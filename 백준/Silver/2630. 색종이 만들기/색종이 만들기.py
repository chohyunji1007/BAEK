def init(N):
    return [[0 for _ in range(N)] for _ in range(N)]

blue_paper = 0
white_paper = 0

def cut_paper(N, x, y, Matrix):
    global blue_paper, white_paper
    
    if N == 1:
        if Matrix[x][y] == 1:
            blue_paper += 1
        else:
            white_paper += 1
    else:
        temp = sum(Matrix[i][j] for i in range(x, x+N) for j in range(y, y+N))
        if temp == 0:
            white_paper += 1
        elif temp == N * N:
            blue_paper += 1
        else:
            N //= 2
            cut_paper(N, x, y, Matrix)
            cut_paper(N, x + N, y, Matrix)
            cut_paper(N, x, y + N, Matrix)
            cut_paper(N, x + N, y + N, Matrix)

def main():
    global blue_paper, white_paper

    N = int(input())
    Matrix = init(N)
    
    for i in range(N):
        row = list(map(int, input().split()))
        for j in range(N):
            if row[j] == 1:
                Matrix[i][j] = 1

    cut_paper(N, 0, 0, Matrix)

    print(white_paper)
    print(blue_paper)

if __name__ == "__main__":
    main()