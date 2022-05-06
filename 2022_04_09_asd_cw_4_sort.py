# arr1 = [1, 3, 4, 6, 47, 67, 99]
# arr2 = [2]

arr2 = [1, 3, 4, 6, 47, 67, 99]
arr1 = [2]

# arr1 = [1, 3, 4, 6]
# arr2 = [2, 5, 7, 8]

print("Tablica 1:")
print(arr1)
print("Tablica 2:")
print(arr2)
print("\n* * *\n")

dl = len(arr1) + len(arr2)

arr_sort = []

while dl > 0:

    while len(arr1) > 0 and (len(arr2) == 0 or arr1[0] < arr2[0]):
        arr_sort.append(arr1[0])
        arr1.pop(0)
        dl = dl - 1

    while len(arr2) > 0 and (len(arr1) == 0 or arr2[0] < arr1[0]):
        arr_sort.append(arr2[0])
        arr2.pop(0)
        dl = dl - 1

print(arr_sort)