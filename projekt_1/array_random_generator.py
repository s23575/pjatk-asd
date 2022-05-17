from numpy import load
from numpy import random
from numpy import save

arr_test = random.randint(1, 100, 10)
arr = random.randint(1, 100, 500000)

save("array_test_random.npy", arr_test)
save("array_random.npy", arr)

arr_test = random.randint(1, 100, 10)
arr = random.randint(1, 100, 500000)

arr_test.sort(kind="stable")
arr.sort(kind="stable")

save("array_test_ascending.npy", arr_test)
save("array_ascending.npy", arr)

arr_test = random.randint(1, 100, 10)
arr = random.randint(1, 100, 500000)

arr_test[::-1].sort(kind="stable")
arr[::-1].sort(kind="stable")

save('array_test_descending.npy', arr_test)
save('array_descending.npy', arr)

print("- - - Dane testowe: - - -")
print(load("array_test_random.npy"))
print(load("array_test_ascending.npy"))
print(load("array_test_descending.npy"))

print("\n- - - Dane wejściowe: - - -")
print(load("array_random.npy"))
print(load("array_ascending.npy"))
print(load("array_descending.npy"))
