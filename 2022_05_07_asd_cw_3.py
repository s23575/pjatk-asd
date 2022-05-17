arr = [5, 4, -1, -7, -4, -3, 2, 4, 6, 8, 9, 10]

print(arr)
print("* * * ")

l = len(arr)
x = True

while(x):
    x = False
    for i in range(0, l-1):
        if arr[i + 1] > 0 and arr[i] < 0:
            arr[i + 1], arr[i] = arr[i], arr[i + 1]
            x = True
        print(arr)

print("* * * ")
print(arr)
