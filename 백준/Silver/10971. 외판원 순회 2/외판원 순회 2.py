def travel_city(city_board, visited, current, count, cost):
    global min_cost

    if count == N - 1:
        if city_board[current][0] != 0:  
            min_cost = min(min_cost, cost + city_board[current][0])
            
        return

    for i in range(N):
        if not visited[i] and city_board[current][i] != 0:
            visited[i] = True
            travel_city(city_board, visited, i, count + 1, cost + city_board[current][i])
            visited[i] = False
       

N = int(input())
city_board = []


for i in range(N):
    row = list(map(int, input().split()))
    city_board.append(row)

visited = [False] * N
visited[0] = True
min_cost = float('inf')

travel_city(city_board, visited, 0, 0, 0)


print(min_cost)