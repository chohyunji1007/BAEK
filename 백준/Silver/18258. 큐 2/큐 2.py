from collections import deque

input_list=[]

for i in range(0,int(input())):
    input_list.append(input())

# push X: 정수 X를 큐에 넣는 연산이다.
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 큐에 들어있는 정수의 개수를 출력한다.
# empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
# front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

deq = deque()

for value in input_list:
   
    if 'push' in value:
        deq.append(value.split()[1])
        
    elif 'pop' in value:
        if len(deq)==0:
            print(-1)
        else:
            print(deq.popleft())
            
    elif 'size' in value:
        # print('deq=',deq)
        print(len(deq))

    elif 'empty' in value:
        if len(deq)==0:
            print(1)
        else:
            print(0)

    elif 'front' in value:
        if len(deq)==0:
            print(-1)
        else:
            print(deq[0])

    elif 'back' in value:
        if len(deq)==0:
            print(-1)
        else:
            print(deq[-1])
