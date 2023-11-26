string = list(map(str,input()))
for i in range(len(string)):
    string[i] = string[i].upper()

check_arr=[]
check_count=[]
for i in range(len(string)):
    if string[i] not in check_arr:
        check_arr.append(string[i])
        check_count.append(1)
    elif string[i] in check_arr:
        check_count[check_arr.index(string[i])] +=1

if check_count.count(max(check_count))>1:
    print("?")
else:
    index = check_count.index(max(check_count))
    print(check_arr[index])