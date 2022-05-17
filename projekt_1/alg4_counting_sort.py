from sys import setrecursionlimit
from time import time

from numpy import load


def counting_sort(arr):
    k = max(arr) + 2
    arr_temp = [0] * k
    arr_sorted = [0] * len(arr)

    for j in range(0, len(arr)):
        arr_temp[arr[j]] = arr_temp[arr[j]] + 1

    for i in range(0, k):
        arr_temp[i] = arr_temp[i] + arr_temp[i - 1]

    for j in range(len(arr) - 1, -1, -1):
        arr_sorted[arr_temp[arr[j]] - 1] = arr[j]
        arr_temp[arr[j]] = arr_temp[arr[j]] - 1

    for i in range(0, len(arr)):
        arr[i] = arr_sorted[i]


setrecursionlimit(10 ** 6)

print("- - - Dane testowe: - - -")

print("Losowe:")
arr_test = load("array_test_random.npy")
print(arr_test)
counting_sort(arr_test)
print(arr_test)

print("Posortowane:")
arr_test = load("array_test_ascending.npy")
print(arr_test)
counting_sort(arr_test)
print(arr_test)

print("Odwrotnie posortowane:")
arr_test = load("array_test_descending.npy")
print(arr_test)
counting_sort(arr_test)
print(arr_test)

print("\n- - - Dane wejściowe: - - -")

print("Losowe:")
arr = load("array_random.npy")
print(arr)
start_time = time()
counting_sort(arr)
end_time = time() - start_time
print(arr)
print("Czas działania: %s seconds" % end_time)

print("Posortowane:")
arr = load("array_ascending.npy")
print(arr)
start_time = time()
counting_sort(arr)
end_time = time() - start_time
print(arr)
print("Czas działania: %s seconds" % end_time)

print("Odwrotnie posortowane:")
arr = load("array_descending.npy")
print(arr)
start_time = time()
counting_sort(arr)
end_time = time() - start_time
print(arr)
print("Czas działania: %s seconds" % end_time)
