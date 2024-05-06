def main():
    vKeyword = input("Enter keyword for Vigenere Table: ")
    vTable = createVigenereTable(vKeyword)
    vdict = createDict(vTable[0])
    # printTable(vTable)
    # print(vdict)

    keyword = input("Enter keyword for Encryption: ").upper()


    while(True):
        choice = input("Encrypt or Decrypt? (E/D): ").upper()
        if choice =='E':
            plaintext = input("Enter plaintext: ").upper()
            ciphertext = encrypt(plaintext, keyword, vTable, vdict)
            print("Ciphertext: ", ciphertext)
        elif choice == 'D':
            ciphertext = input("Enter ciphertext: ").upper()
            plaintext = decrypt(ciphertext, keyword, vTable, vdict)
            print("Plaintext: ", plaintext)
        elif choice == "EXIT":
            break


def encrypt(plaintext, keyword, table, dict):
    ciphertext = ""
    for key in plaintext:
        # print(table[dict[key]][dict[keyword[0]]])
        ciphertext += table[dict[key]][dict[keyword[0]]]
        keyword = shiftKeyword(keyword, 1)

    return ciphertext


def decrypt(ciphertext, keyword, table, dict):
    plaintext = ""
    for key in ciphertext:
        alphabet = createAlphabet(keyword[0], dict)
        # print(alphabet)
        ciphertext_index = alphabet.index(key)
        # print(ciphertext_index)
        plaintext += table[0][ciphertext_index]
        # print(plaintext)
        keyword = shiftKeyword(keyword, 1)
    return plaintext


def shiftKeyword(keyword, shift):
    shiftedKeyword = keyword[shift:] + keyword[:shift]
    # print(shiftedKeyword)
    return shiftedKeyword


# def find_plaintext(table, keyword_char, ciphertext_index, dict):
#     for key, value in dict.items():
#         if value == keyword_char:
#             for row in table:
#                 if row[0] == key:
#                     return row[ciphertext_index]


def createAlphabet(key, dict):
    alphabet = ""
    swapped_dict = swapDict(dict)
    # print(key)
    # print(dict)
    # print(swapped_dict)
    start_value = dict[key]
    for i in range(26):
        next_value = (start_value + i) % 26  
        alphabet += swapped_dict[next_value]
    return alphabet


def createVigenereTable(keyword):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    keyword = keyword.upper()
    for letter in keyword:
        alphabet = alphabet.replace(letter, "")
    alphabet = keyword + alphabet

    table = []
    for i in range(26):
        table.append(alphabet[i:] + alphabet[:i])
    return table


def createDict(List):
    dict = {}
    for i, key in enumerate(List):
        dict[key] = i
    return dict


def swapDict(dict):
    swapped_dict = {value: key for key, value in dict.items()}
    # print(swapped_dict)
    return swapped_dict


def printTable(table):
    for row in table:
        print(row)


if __name__ == '__main__':
    main()


