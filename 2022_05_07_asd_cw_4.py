def mergesort(arr):
    if len(arr) > 1:

        half = len(arr)//2
        left = arr[:half]
        right = arr[half:]

        mergesort(left)
        mergesort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

arr = [12, 7, 3, 8, 15, 3, 8, 12]

print(arr)
print("* * *")
mergesort(arr)
print("* * *")
print(arr)