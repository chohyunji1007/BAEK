import sys
input = sys.stdin.readline
m = int(input()) #연산 수
s = set()
for _ in range(m):
    code = input().split()
    get_code = code[0]
    if get_code!="all" and get_code!="empty":
        get_x = int(code[1])
    # print (get_code," ", get_x)
    if get_code == "add" and get_x not in s:
        s.add(get_x)
    elif get_code == "remove" and get_x in s:
        s.remove(get_x)
    elif get_code == "check":
        # print("s=",s)
        if get_x not in s:
            print("0")
        else:
            print("1")
    elif get_code == "toggle":
        if get_x in s:
            s.remove(get_x)
        else:
            s.add(get_x)
    elif get_code == "all":
        s.clear()
        s = {i for i in range (1,21)}
    elif get_code == "empty":
        s.clear()