import random
from os import system

from functions import header
from variables import (char_list, cripto_letters, decrypt_text, encrypt_text,
                       letters_list, password)

# this function will assign
# a new character to the original character
for char in letters_list:
    while True:
        new_char = random.choice(char_list)
        if new_char not in cripto_letters.values() and new_char != char:
            cripto_letters[char] = new_char
            break

# inputs
while True:
    header('🔗 Enter with your text:')
    text = list(input("➡  "))
    for char in text:
        error_count = 0  # this variable will verify if have some char from text not in list
        if char not in char_list:
            error_count += 1
            header('ERROR TO ENCRYPT')
            print(f'❌ Not is possible to encrypt the characther "{char}".')
            print('❌ Try again.')
    if error_count == 0:  # if not had some char not in list finish the loop
        break
system('cls')

# Encrypting the menssage
header("🔒 Follows encrypted text:")
for ind, letter in enumerate(text):
    text[ind] = cripto_letters[letter]
    encrypt_text += cripto_letters[letter]
print(f'✅ {encrypt_text}', end='\n\n')


# Requires the password for decrypting the menssage
while True:
    header('🔑 Enter with password to decrypt the text:')
    password_confirmation = input()
    if password_confirmation != password:
        print("❌ Password is wrong. You can't decrypt the mensage\n")
    else:
        break

# Decrypting the menssage
for ind, letter in enumerate(text):
    for key, value in cripto_letters.items():
        if letter == value:
            decrypt_text += key
header("🔓 The text sending was:")
print(f'✅ {decrypt_text}', end='\n\n')
