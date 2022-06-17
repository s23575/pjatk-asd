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


# Kodowanie danego znaku za pomocą zera lub jedynki (w zależności od jego ścieżki (lewa / prawa) w drzewie binarnym):
def leaf_bin(string, side, dict):
    for char in string:
        if char in dict:
            dict[char] = side + dict[char]
        else:
            dict[char] = side


# Tworzenie słownika:
def huffman_dict_bin(freq):
    queue = [list(freq.keys()), list(freq.values())]
    dict = {}

    # Tworzenie słownika:
    for i in range(len(queue[0]) - 1):
        build_min_heap(queue)
        leaf_left = [queue[0].pop(0), queue[1].pop(0)]
        leaf_bin(leaf_left[0], "0", dict)

        build_min_heap(queue)
        leaf_right = [queue[0].pop(0), queue[1].pop(0)]
        leaf_bin(leaf_right[0], "1", dict)

        node = [leaf_left[0] + leaf_right[0], leaf_left[1] + leaf_right[1]]
        queue[0].insert(0, node[0])
        queue[1].insert(0, node[1])

    return dict


def huffman_encoding(dict, string):
    string_bin = ""
    for char in string:
        string_bin += dict[char]
    return string_bin


# Tablica n znaków:
with open("text_to_encode", "r") as f:
    string = f.read()
print(string)

# Tablica częstotliwości występowania n znaków:
freq = {}
for char in string:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

dict = huffman_dict_bin(freq)
print(dict)

string_bin = huffman_encoding(dict, string)
print(string_bin)

n = 8
str_arr = [string_bin[i:i + n] for i in range(0, len(string_bin), n)]
last = "{" + str_arr[-1] + "}"
str_arr.pop()

file = open("text_to_decode", "w")
file.write(str(dict) + "[COMPRESSED_TEXT]")
file.close()
file = open("text_to_decode", "ab")
for bit in str_arr:
    n = int(bit, 2)
    data = bytes([n])
    file.write(data)
file.close()
file = open("text_to_decode", "a")
file.write("[COMPRESSED_TEXT]" + last)
file.close()

