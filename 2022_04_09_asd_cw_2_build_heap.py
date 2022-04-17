import math


def max_heapify(K, i):
    left = i * 2 + 1
    right = left + 1
    length = len(K)

    if left < length and K[left] > K[i]:
        largest = left
    else:
        largest = i

    if right < length and K[right] > K[largest]:
        largest = right

    if largest != i:
        K[i], K[largest] = K[largest], K[i]
        max_heapify(K, largest)

    return K


def build_max_heap(K):
    heap_size = len(K)
    for i in range(math.floor(heap_size / 2), -1, -1):
        max_heapify(K, i)
    return K


# arr = [50,9,8,7,2,1,7,4,4]
arr = [12, 6, 33, 4, 6, 11]

print("Tablica:")
print(arr)
print("\n* * *\n")

print(build_max_heap(arr))
