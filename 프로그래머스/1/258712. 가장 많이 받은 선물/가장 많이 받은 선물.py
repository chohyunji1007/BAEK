def solution(friends, gifts):
    answer = 0
    get_maps, get_arr = fun1(friends, gifts)
    # print(get_arr)
    answer = check(friends,get_maps, get_arr)
    return answer

def fun1(friends, gifts):
    len_friends = len(friends)
    len_gifts = len(gifts)
    maps =[[0]*len_friends for _ in range(len_friends)]
    arr = [[0]*3 for _ in range(len_friends)]
    
    
    for i in range(len_gifts):
        send, receive = gifts[i].split()
        maps[friends.index(send)][friends.index(receive)] += 1
        arr[friends.index(send)][0] += 1
        arr[friends.index(receive)][1] += 1
    for i in range(len(arr)):
        arr[i][2] = arr[i][0] - arr[i][1]
    
    return maps, arr

def check(friends,maps, arr):
    # print(len(arr))
    
    len_arr = len(arr)
    arr2 = [0] * len_arr
    for i in range(len_arr):
        for j in range(1,len(maps)):
            
            if i<j:
                print(i, j)
                if maps[i][j] > maps[j][i] :
                    print("1."+friends[i]+"가 "+ friends[j]+"보다 "+str(maps[i][j]-maps[j][i])+"개 선물을 더줘서 +1")
                    arr2[i]+=1
                elif maps[i][j] < maps[j][i]:
                    print("2."+friends[j]+"가 "+ friends[i]+"보다 "+str(maps[i][j]-maps[j][i])+"개 선물을 더줘서 +1")
                    arr2[j]+=1
                else:
                    if arr[i][2] > arr[j][2]:
                        print(friends[i]+"와 "+friends[j]+"보다 선물지수가 더 높아서 +1")
                        arr2[i]+=1
                    elif arr[i][2] < arr[j][2]:
                        print(friends[j]+"와 "+friends[i]+"보다 선물지수가 더 높아서 +1")
                        arr2[j]+=1
                    else:
                        print(friends[i]+"와 "+friends[j]+"는 선물지수 같아서 아무것도 안함")
    # print(arr2)
    return max(arr2)
    

