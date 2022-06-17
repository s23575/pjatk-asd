import ast


def huffman_decoding(str_dict, str_bin):
    dict = ast.literal_eval(str_dict)

    decoding = [list(dict.keys()), list(dict.values())]
    string_search = ""
    decoded = ""

    for i in range(len(string_bin)):
        string_search += string_bin[i]
        if string_search in decoding[1] and (
                i + 1 == len(string_bin) or not string_search + string_bin[i + 1] in decoding[1]):
            decoded += decoding[0][decoding[1].index(string_search)]
            string_search = ""

    return decoded


with open("text_to_decode", "r", errors='ignore') as f:
    string = f.read()

string = string.split("[COMPRESSED_TEXT]")

str_dict = string[0]

with open("text_to_decode", "rb") as f:
    byte_array = f.read()

compressed_text_start = len(string[0]) + len("[COMPRESSED_TEXT]")
compressed_text_end = len(byte_array) - (len("[COMPRESSED_TEXT]") + len(string[2]))

string_bin = ""

for x in range(compressed_text_start, compressed_text_end):
    string_bin += format(byte_array[x], '#010b')[2:]

string_bin += string[2][1:-1]

decoded = huffman_decoding(str_dict, string_bin)
print(decoded)
