import math


# Budowanie kolejki priorytetowej typu minimum ("kopcowanie"):
def min_heapify(arr, i):
    left = i * 2 + 1
    right = left + 1
    length = len(arr[0])

    if left < length and arr[1][left] < arr[1][i]:
        smallest = left
    else:
        smallest = i

    if right < length and arr[1][right] < arr[1][smallest]:
        smallest = right

    if smallest != i:
        arr[0][i], arr[0][smallest] = arr[0][smallest], arr[0][i]
        arr[1][i], arr[1][smallest] = arr[1][smallest], arr[1][i]
        min_heapify(arr, smallest)

    return arr


# Budowanie kolejki priorytetowej typu minimum:
def build_min_heap(arr):
    heap_size = len(arr[0])
    for i in range(math.floor(heap_size / 2), -1, -1):
        min_heapify(arr, i)
    return arr


def leaf_bin(string, side):
    for char in string:
        if char in dict:
            dict[char] = side + dict[char]
        else:
            dict[char] = side


# Tablica n znaków:
string = "Ala ma kota"
# Tablica częstotliwości występowania n znaków:
freq = {}
for char in string:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

# Dwuwymiarowa tablica zawierająca n znaków (1. wymiar) i częstotliwość ich występowania (2. wymiar):
queue = [list(freq.keys()), list(freq.values())]
dict = {}

for i in range(len(queue[0]) - 1):
    build_min_heap(queue)
    leaf_left = [queue[0].pop(0), queue[1].pop(0)]
    leaf_bin(leaf_left[0], "0")

    build_min_heap(queue)
    leaf_right = [queue[0].pop(0), queue[1].pop(0)]
    leaf_bin(leaf_right[0], "1")

    node = [leaf_left[0] + leaf_right[0], leaf_left[1] + leaf_right[1]]
    queue[0].insert(0, node[0])
    queue[1].insert(0, node[1])

print(dict)

string_bin = ""

for char in string:
    string_bin += dict[char]

print(string_bin)

string_search = ""

decoding = [list(dict.keys()), list(dict.values())]

decoded = ""

for i in range(len(string_bin)):
    string_search += string_bin[i]
    if string_search in decoding.value:
        if not i + 1 == len(string_bin):
            if not string_search + string_bin[i + 1] in decoding[1]:
                decoded += decoding[0][decoding[1].index(string_search)]
                string_search = ""
        else:
            decoded += decoding[0][decoding[1].index(string_search)]
            string_search = ""

print(decoded)
