data_len,A = int(input()),sorted(map(int, input().split()))
data_len2,B = int(input()),input().split()

def binary_search(target, data):
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return 1
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid -1

    return 0

for value in B:
    print(binary_search(int(value),A))