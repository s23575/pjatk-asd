arr = [5,4,3,2,1,0]
print("Tablica:")
print(arr)
print("\n* * *\n")

print("Sortowanie przez wstawianie:")

for j in range (1, len(arr)):
    j_value = arr[j]
    i = j - 1

    while i > -1 and arr[i] > j_value:
        arr[i + 1] = arr[i]
        i = i - 1
        print(arr)

    arr[i + 1] = j_value

print("Posortowane:")
print(arr)
print("\n* * *\n")

# # #

arr = [5,4,3,2,1,0]
print("Tablica:")
print(arr)
print("\n* * *\n")

print("Sortowanie bąbelkowe:")

for i in range(1, len(arr)):
    for j in range(0, i):
        if arr[j] > arr[i]:
            arr[j], arr[i] = arr[i], arr[j]
        print(arr)

print("Posortowane:")
print(arr)
print("\n* * *\n")

# # #

arr = [5,4,3,2,1,0]
print("Tablica:")
print(arr)
print("\n* * *\n")

print("Sortowanie bąbelkowe z plusem:")

for i in range(1, len(arr)):
    flag = False
    if not flag:
        for j in range(0, i):
            if arr[j] > arr[i]:
                arr[j], arr[i] = arr[i], arr[j]
            else:
                flag = True
        print(arr)

print("Posortowane:")
print(arr)
print("\n* * *\n")