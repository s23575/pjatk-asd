from sys import setrecursionlimit
from time import time

from numpy import load


def partition(arr, p, r):
    x = arr[r]
    i = p - 1

    for j in range(p, r):
        if arr[j] <= x:
            i = i + 1
            arr[j], arr[i] = arr[i], arr[j]

    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1


# def quicksort(arr, p, r):
#     if p < r:
#         q = partition(arr, p, r)
#         quicksort(arr, p, q - 1)
#         quicksort(arr, q + 1, r)

def quicksort(arr, p, r):
    while p < r:
        q = partition(arr, p, r)
        quicksort(arr, p, q - 1)
        p = q + 1


setrecursionlimit(10 ** 6)

print("- - - Dane testowe: - - -")

print("Losowe:")
arr_test = load("array_test_random.npy")
print(arr_test)
quicksort(arr_test, 0, len(arr_test) - 1)
print(arr_test)

print("Posortowane:")
arr_test = load("array_test_ascending.npy")
print(arr_test)
quicksort(arr_test, 0, len(arr_test) - 1)
print(arr_test)

print("Odwrotnie posortowane:")
arr_test = load("array_test_descending.npy")
print(arr_test)
quicksort(arr_test, 0, len(arr_test) - 1)
print(arr_test)

print("\n- - - Dane wejściowe: - - -")

print("Losowe:")
arr = load("array_random.npy")
print(arr)
start_time = time()
quicksort(arr, 0, len(arr) - 1)
end_time = time() - start_time
print(arr)
print("Czas działania: %s seconds" % end_time)

print("Posortowane:")
arr = load("array_ascending.npy")
print(arr)
start_time = time()
quicksort(arr, 0, len(arr) - 1)
end_time = time() - start_time
print(arr)
print("Czas działania: %s seconds" % end_time)

print("Odwrotnie posortowane:")
arr = load("array_descending.npy")
print(arr)
start_time = time()
quicksort(arr, 0, len(arr) - 1)
end_time = time() - start_time
print(arr)
print("Czas działania: %s seconds" % end_time)
