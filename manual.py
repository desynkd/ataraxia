import myfunctions as myfunc

def main():
    vKeyword = input("Enter keyword for Vigenere Table: ")
    vTable = myfunc.createVigenereTable(vKeyword)
    vdict = myfunc.createDict(vTable[0])
    # myfunc.printTable(vTable)

    keyword = input("Enter keyword for Encryption: ").upper()

    while(True):
        choice = input("Encrypt or Decrypt? (E/D): ").upper()
        if choice =='E':
            plaintext = input("Enter plaintext: ").upper()
            ciphertext = myfunc.encrypt(plaintext, keyword, vTable, vdict)
            print("Ciphertext: ", ciphertext.lower())
        elif choice == 'D':
            ciphertext = input("Enter ciphertext: ").upper()
            plaintext = myfunc.decrypt(ciphertext, keyword, vTable, vdict)
            print("Plaintext: ", plaintext.lower())
        elif choice == "EXIT":
            break


if __name__ == '__main__':
    main()


