import math
import os

import numpy
from numpy import save


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



#
# n = int(string_bin, 2)
# n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
#
# # b = string_bin
# # a_byte_array = bytearray(int(b[x:x+8], 2) for x in range(0, len(b), 8))
# # print(a_byte_array)
# #
# # file = open("sample", "wb")
# # # file.write(bytearray(str(dict).encode('ascii')))
# # file.seek(0, os.SEEK_END)
# # file.write(a_byte_array)
# # file.close()