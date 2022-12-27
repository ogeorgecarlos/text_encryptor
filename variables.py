import string

password = 'something'
encrypt_text = ''
decrypt_text = ' '

# A list with alphanumerics availlable to enter a text
letters_list = list(string.printable)
accent = "Á", "á", "À", "à", "Â", "â", "Ä", "ä", "Ã", "ã", "Å", "å", "Æ", "æ", "Ç", "ç", "Ð", "ð", "É", "é", "È", "è", "Ê", "ê", "Ë", "ë", "Í", "í", "Ì", "ì", "Î",	"î", "Ï", "ï", "Ñ",	"ñ", "Ó", "ó", "Ò",	"ò", "Ô", "ô", "Ö",	"ö", "Õ", "õ", "Ø", "ø", "Ú", "ú", "Ù", "ù", "Û", "û", "Ü", "ü", "Ý", "ý", " "
accent_list = list(accent)
letters_list.extend(accent)

# A list with all printables (letters, numbers, punctuations)
# that will replace the original characters from text
char_list = list(string.printable)
char_list.extend(accent_list)
char_list.append("10")
print(len(char_list))

# A Dict that will store the new configuration for each char
cripto_letters = dict()
