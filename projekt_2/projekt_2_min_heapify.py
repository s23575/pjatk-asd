import math


def min_heapify(arr, i):
    left = i * 2 + 1
    right = left + 1
    length = len(arr)

    if left < length and arr[left] < arr[i]:
        smallest = left
    else:
        smallest = i

    if right < length and arr[right] < arr[smallest]:
        smallest = right

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        min_heapify(arr, smallest)

    return arr


def build_min_heap(arr):
    heap_size = len(arr)
    for i in range(math.floor(heap_size / 2), -1, -1):
        min_heapify(arr, i)
    return arr
