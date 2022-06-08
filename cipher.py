import os
import time

def encoder (string, shift):

    encoded_word = ""
    for letter in string:

        if (ord(letter) in range (65,91)) or (ord(letter) in range (97,123)):

            if letter.isupper():
                output_letter = ord(letter) + shift
                if output_letter > 90:
                    output_letter -= 26

            elif letter.islower():
                output_letter = ord(letter) + shift
                if output_letter > 122:
                    output_letter -= 26

            encoded_word += chr(output_letter)
        else:
            encoded_word += letter

    print (encoded_word)


def decoder (string, shift):

    decoded_word = ""
    for letter in string:
        if (ord(letter) in range (65,91)) or (ord(letter) in range (97,123)):

            if letter.isupper():
                output_letter = ord(letter) - shift
                if output_letter < 65:
                    output_letter += 26
            
            elif letter.islower():
                output_letter = ord(letter) - shift
                if output_letter < 97:
                    output_letter += 26

            decoded_word += chr(output_letter)
        else:
            decoded_word += letter

    print (decoded_word)

if __name__ == "__main__":

    os.system('cls')
    welcome_message = "WELCOME TO CEASER CIPHER !!"
    for letter in welcome_message:
        print (letter, end="", flush=True)
        time.sleep(0.1)
    print('\n')

    while True:

        encode_decode = input ("Enter the operation to be performed (encode/decode)\n")
        input_message = input("Enter the message to be encoded/decode :")
        shift = int(input("Enter the shift :"))
        shift = shift % 26

        if encode_decode.lower() == 'encode':
            encoder(string=input_message, shift=shift)
        
        elif encode_decode.lower() == 'decode':
            decoder(input_message, shift)
        
        choice = input ("Do you want to continue (y/n):")
        if choice.lower() != 'y':
            break
