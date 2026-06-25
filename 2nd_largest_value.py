arr = [3, 2, 1, 5, 6, 4]
k = 2

for i in range(len(arr)):
    for j in range(i+1, len(arr)):

        if arr[i] < arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

print(arr[k-1])            