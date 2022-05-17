arr = [-7, -4, -3, 2, 4, 6, 8, 9, 10]

print("Tablica:")
print(arr)

for i in range(0, len(arr)-1):
    if i % 2 == 0 and arr[i] < arr[i+1]:
        arr[i], arr[i+1] = arr[i+1], arr[i]

print("Tablica po przerobieniu:")
print(arr)
