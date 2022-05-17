from math import floor
from sys import setrecursionlimit
from time import time

from numpy import load


def max_heapify(arr, length, i):
    largest = i
    left = i * 2 + 1
    right = left + 1

    if left < length and arr[left] > arr[i]:
        largest = left

    if right < length and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, length, largest)


def build_max_heap(arr):
    heap_size = len(arr)
    for i in range(floor(heap_size / 2), -1, -1):
        max_heapify(arr, heap_size, i)


def heap_sort(arr):
    build_max_heap(arr)

    for i in range(len(arr) - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        max_heapify(arr, i, 0)


setrecursionlimit(10 ** 6)

print("- - - Dane testowe: - - -")

print("Losowe:")
arr_test = load("array_test_random.npy")
print(arr_test)
heap_sort(arr_test)
print(arr_test)

print("Posortowane:")
arr_test = load("array_test_ascending.npy")
print(arr_test)
heap_sort(arr_test)
print(arr_test)

print("Odwrotnie posortowane:")
arr_test = load("array_test_descending.npy")
print(arr_test)
heap_sort(arr_test)
print(arr_test)

print("\n- - - Dane wejściowe: - - -")

print("Losowe:")
arr = load("array_random.npy")
print(arr)
start_time = time()
heap_sort(arr)
end_time = time() - start_time
print(arr)
print("Czas działania: %s seconds" % end_time)

print("Posortowane:")
arr = load("array_ascending.npy")
print(arr)
start_time = time()
heap_sort(arr)
end_time = time() - start_time
print(arr)
print("Czas działania: %s seconds" % end_time)

print("Odwrotnie posortowane:")
arr = load("array_descending.npy")
print(arr)
start_time = time()
heap_sort(arr)
end_time = time() - start_time
print(arr)
print("Czas działania: %s seconds" % end_time)
