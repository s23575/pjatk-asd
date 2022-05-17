import math

def max_heapify(K, length, i):
    left = i * 2 + 1
    right = left + 1

    if left < length and K[left] > K[i]:
        largest = left
    else:
        largest = i

    if right < length and K[right] > K[largest]:
        largest = right

    if largest != i:
        K[i], K[largest] = K[largest], K[i]
        max_heapify(K, length, largest)

    return K


def build_max_heap(K):
    heap_size = len(K)
    for i in range(math.floor(heap_size / 2), -1, -1):
        max_heapify(K, heap_size, i)

    return K


def sort_heap(K, i):
    K = build_max_heap(K)
    print(K)
    for j in range(len(K) - 1, i - 1, -1):
        print(j, " ", K)
        K[j], K[0] = K[0], K[j]
        print(j, " ", K)
        K = max_heapify(K, j, 0)
        print(j, " ", K)
        print("")

    return K[len(K) - i]


def element(K, i):
    x = K[len(arr) - i]
    return x


arr = [12, 6, 33, 4, 6, 11]
# arr = [7,2,1,4,9,8,7,4]
# arr = [50,9,8,7,2,1,7,4,4]
# arr = [50,9,8,7,2,1,7,4,8]
# arr = [50,9,8,7,2,1,7,4,4,2]

print("Tablica:")
print(arr)
print("\n* * *\n")

print(sort_heap(arr, 3))
