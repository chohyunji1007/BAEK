input_list=[]
stack=[]
for i in range(0,int(input())):
    input_list.append(input())
# print(input_list[0].split())

for value in input_list:
    # print('value=',value)
    if 'push' in value:
        stack.append(value.split()[1])

    elif 'pop' in value:
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])
            del stack[-1]

    elif 'size' in value:
        print(len(stack))

    elif 'empty' in value:
        if len(stack)==0:
            print(1)
        else:
            print(0)
            
    elif 'top' in value:
        if len(stack)==0:
            print(-1)
        else:
            print(stack[len(stack)-1])