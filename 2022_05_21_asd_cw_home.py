import time


def countingSort(arr, k):
    arrTemp = [0] * k
    arrSorted = [0] * len(arr)

    for j in range(0, len(arr)):
        arrTemp[arr[j]] = arrTemp[arr[j]] + 1

    for i in range(0, k):
        arrTemp[i] = arrTemp[i] + arrTemp[i - 1]

    for j in range(len(arr) - 1, -1, -1):
        arrSorted[arrTemp[arr[j]] - 1] = arr[j]
        arrTemp[arr[j]] = arrTemp[arr[j]] - 1

    for i in range(0, len(arr)):
        arr[i] = arrSorted[i]


arr = [12, 7, 3, 8, 15, 3, 8, 12]
k = max(arr) + 2

print(arr)
print("* * *")

countingSort(arr, k)

print(arr)
