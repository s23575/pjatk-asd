from math import floor
from sys import setrecursionlimit
from time import time

from numpy import load


def merge_sort(arr):
    length = len(arr)
    if length > 1:

        half = floor(length / 2)
        left = arr[:half].copy()
        right = arr[half:].copy()

        merge_sort(left)
        merge_sort(right)

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


setrecursionlimit(10 ** 6)

print("- - - Dane testowe: - - -")

print("Losowe:")
arr_test = load("array_test_random.npy")
print(arr_test)
merge_sort(arr_test)
print(arr_test)

print("Posortowane:")
arr_test = load("array_test_ascending.npy")
print(arr_test)
merge_sort(arr_test)
print(arr_test)

print("Odwrotnie posortowane:")
arr_test = load("array_test_descending.npy")
print(arr_test)
merge_sort(arr_test)
print(arr_test)

print("\n- - - Dane wejściowe: - - -")

print("Losowe:")
arr = load("array_random.npy")
print(arr)
start_time = time()
merge_sort(arr)
end_time = time() - start_time
print(arr)
print("Czas działania: %s seconds" % end_time)

print("Posortowane:")
arr = load("array_ascending.npy")
print(arr)
start_time = time()
merge_sort(arr)
end_time = time() - start_time
print(arr)
print("Czas działania: %s seconds" % end_time)

print("Odwrotnie posortowane:")
arr = load("array_descending.npy")
print(arr)
start_time = time()
merge_sort(arr)
end_time = time() - start_time
print(arr)
print("Czas działania: %s seconds" % end_time)
