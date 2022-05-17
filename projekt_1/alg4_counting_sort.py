from time import time
from numpy import load


def counting_sort(arr, k):
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


print("- - - Dane testowe: - - -")

print("Losowe:")
arr_test = load("array_test_random.npy")
k = max(arr_test) + 2
print(arr_test)
counting_sort(arr_test, k)
print(arr_test)

print("Posortowane:")
arr_test = load("array_test_ascending.npy")
k = max(arr_test) + 2
print(arr_test)
counting_sort(arr_test, k)
print(arr_test)

print("Odwrotnie posortowane:")
arr_test = load("array_test_descending.npy")
k = max(arr_test) + 2
print(arr_test)
counting_sort(arr_test, k)
print(arr_test)

print("\n- - - Dane wejściowe: - - -")

print("Losowe:")
arr = load("array_random.npy")
print(arr)
start_time = time()
k = max(arr) + 2
counting_sort(arr, k)
end_time = time() - start_time
print(arr)
print("Czas działania: %s seconds" % end_time)

print("Posortowane:")
arr = load("array_ascending.npy")
print(arr)
start_time = time()
k = max(arr) + 2
counting_sort(arr, k)
end_time = time() - start_time
print(arr)
print("Czas działania: %s seconds" % end_time)

print("Odwrotnie posortowane:")
arr = load("array_descending.npy")
print(arr)
start_time = time()
k = max(arr) + 2
counting_sort(arr, k)
end_time = time() - start_time
print(arr)
print("Czas działania: %s seconds" % end_time)