M, N, L = map(int, input().split())
hunters = sorted(map(int, input().split()))

ret = 0
animals = [list(map(int, input().split())) for _ in range(N)]
animals.sort(key=lambda x: x[0])

for animal in animals:
    animal_pos, distance_needed = animal
    left, right = 0, M - 1
    
    while left <= right:
        mid = (left + right) // 2
        if hunters[mid] < animal_pos - (L - distance_needed):
            left = mid + 1
        elif hunters[mid] > animal_pos + (L - distance_needed):
            right = mid - 1
        else:
            ret += 1
            break

print(ret)