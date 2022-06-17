import ast


def huffman_decoding(dictionary, str_bin):
    decoding = [list(dictionary.keys()), list(dictionary.values())]
    string_search = ""
    decoded = ""

    for i in range(len(string_bin)):
        string_search += string_bin[i]
        if string_search in decoding[1] and (
                i + 1 == len(string_bin) or not string_search + string_bin[i + 1] in decoding[1]):
            decoded += decoding[0][decoding[1].index(string_search)]
            string_search = ""

    return decoded


def return_dict_last(file="text_to_decode"):
    with open(file, "r", errors='ignore') as file:
        string = file.read()
    string = string.split("[COMPRESSED_TEXT]")
    str_dict = string[0]
    last = string[2]
    return str_dict, last


def return_string_bin(file="text_to_decode"):
    with open(file, "rb") as file:
        byte_array = file.read()

    compressed_text_start = len(str_dict) + len("[COMPRESSED_TEXT]")
    compressed_text_end = len(byte_array) - (len("[COMPRESSED_TEXT]") + len(last))

    string_bin = ""

    for x in range(compressed_text_start, compressed_text_end):
        string_bin += format(byte_array[x], '#010b')[2:]

    string_bin += last[1:-1]
    return string_bin


str_dict, last = return_dict_last()
dictionary = ast.literal_eval(str_dict)
print("\n[SŁOWNIK]\n")
print(dictionary)

string_bin = return_string_bin()
print("\n[TEKST_DO_ODKODOWANIA]\n")
print(string_bin)

decoded = huffman_decoding(dictionary, string_bin)
print("\n[TEKST_ODKODOWANY]\n")
print(decoded)
