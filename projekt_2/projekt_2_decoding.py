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


string_bin = "01001110110111110110111000100010"
str_dict = "{'A': '010', 'l': '011', 'k': '1110', 'm': '1111', 't': '000', 'o': '001', ' ': '110', 'a': '10'}"

decoded = huffman_decoding(str_dict, string_bin)
print(decoded)
