def binarySearch(arr, x, start, stop):
    if stop >= start:

        mid = start + (stop - start) // 2

        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            return binarySearch(arr, x, start, mid - 1)

        else:
            return binarySearch(arr, x, mid + 1, stop)

    else:
        return -1


arr = [0, 1, 2, 3, 3, 4, 5]
x = 4

y = binarySearch(arr, x, 0, len(arr) - 1)

if y != -1:
    print("Element znajduje się na pozycji: " + str(y))
else:
    print("Nie znaleziono poszukiwanego elementu")
