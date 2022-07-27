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
def leaf_bin(string, side, dictionary):
    for char in string:
        if char in dictionary:
            dictionary[char] = side + dictionary[char]
        else:
            dictionary[char] = side


# Tworzenie słownika:
def huffman_dict_bin(freq):
    queue = [list(freq.keys()), list(freq.values())]
    dictionary = {}
    build_min_heap(queue)

    # Tworzenie słownika:
    for i in range(len(queue[0]) - 1):
        leaf_left = [queue[0].pop(0), queue[1].pop(0)]
        leaf_bin(leaf_left[0], "0", dictionary)
        min_heapify(queue, 0)

        leaf_right = [queue[0].pop(0), queue[1].pop(0)]
        leaf_bin(leaf_right[0], "1", dictionary)
        min_heapify(queue, 0)

        node = [leaf_left[0] + leaf_right[0], leaf_left[1] + leaf_right[1]]
        queue[0].insert(0, node[0])
        queue[1].insert(0, node[1])

    return dictionary


def huffman_encoding(dictionary, string):
    string_bin = ""
    for char in string:
        string_bin += dictionary[char]
    return string_bin


def string_bin_to_char(string_bin):
    n = 8
    str_arr = [string_bin[i:i + n] for i in range(0, len(string_bin), n)]
    last = "{" + str_arr[-1] + "}"
    str_arr.pop()
    return last, str_arr


def save_file(dict, str_arr, last, file="text_to_decode"):
    file = open(file, "w")
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


# Tablica n znaków:
with open("text_to_encode", "r") as f:
    string = f.read()
print("\n[TEKST_DO_ZAKODOWANIA]\n")
print(string)

# Tablica częstotliwości występowania n znaków:
freq = {}
for char in string:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

dictionary = huffman_dict_bin(freq)
print("\n[SŁOWNIK]\n")
print(dictionary)

string_bin = huffman_encoding(dictionary, string)
print("\n[TEKST_ZAKODOWANY]\n")
print(string_bin)

last, str_arr = string_bin_to_char(string_bin)
save_file(dictionary, str_arr, last)
