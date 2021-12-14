def encrypt(string, k):
    result = ""

    for i in range(len(string)):
        char = string[i]

        if char.isupper():
            result += chr((ord(char) + k - 65) % 26 + 65)

        else:
            result += chr((ord(char) + k - 97) % 26 + 97)

    return result


def decrypt(string, k):
    result = ""

    for i in range(len(string)):
        char = string[i]

        if char.isupper():
            result += chr((ord(char) - k - 65) % 26 + 65)

        else:
            result += chr((ord(char) - k - 97) % 26 + 97)

    return result


if __name__ == "__main__":

    print('type encrypt for encryption or decrypt to decryption or exit:')

    choice = input()
    while not choice == 'exit':

        match choice:
            case 'encrypt':
                print('Enter string you would like to encrypt or exit:')
                string = input()
                print('Enter number for the key:')
                k = input()
                print("Text  : " + string)
                print("Encrypted text: " + encrypt(string, int(k)))

                print('type encrypt for encryption or decrypt to decryption:')
                choice = input()

            case 'decrypt':
                print('Enter string you would like to decrypt:')
                string = input()
                print('Enter key:')
                k = input()

                print("Decrypted Text :", decrypt(string, int(k)))
                print('type encrypt for encryption or decrypt to decryption or exit:')
                choice = input()

