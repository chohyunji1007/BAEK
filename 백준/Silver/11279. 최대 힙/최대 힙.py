import heapq

input_list=[]
heap=[]

for i in range(0,int(input())):
    input_list.append(int(input()))
# print(input_list)

for value in input_list:
    # print('heap=',heap)
    if value==0:
        if len(heap)!=0:
            print(-heapq.heappop(heap))
        else:
            print('0')

    else:
        heapq.heappush(heap, -value)
        # print(heap)