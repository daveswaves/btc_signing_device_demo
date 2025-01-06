'''
cd ~/pypo && poetry shell
python src/bip39.py

# Module Installation
pip3 install embit

# Display installed Python modules:
pip3 list

# Check if specific module is installed:
pip3 show <MODULE> eg. pip3 show pyzbar

Docs:
https://embit.rocks
https://github.com/diybitcoinhardware/embit
https://coldbit.com/bip-39-basics-from-randomness-to-mnemonic-words

Check results:
https://iancoleman.io/bip39
'''

from embit import bip39
import os
# from pprint import pprint

seed_phrase = "smoke chimney announce candy glory tongue refuse fatigue cricket once consider beef treat urge wing deny gym robot tobacco adult problem priority wheat diagram"

seed_phrase = "crater cloud drill young animal century earth siren because detail knock unfold error jaguar merry pistol fatigue nation wise clinic boss assault grape dinosaur"

data_list = []
data_list.append(f"+---------+---------+------------+")
data_list.append(f"| Word    | Decimal | Binary     |")
data_list.append(f"+---------+---------+------------+")
full264bit_24word_binary = ''
index_concat = ''
for word in seed_phrase.split(" "):
    index = bip39.WORDLIST.index(word)
    word = word.ljust(8) # pad with trailing spaces to 8 characters
    binary = bin(index)[2:].zfill(11)
    index = "%04d" % index # pad with leading zeros to 4 digits
    data_list.append(f"|{word} |{index}     |{binary} |")
    full264bit_24word_binary += binary
    index_concat += index

data_list.append(f"+---------+---------+------------+")

sha256_private_key_str = full264bit_24word_binary[:-8]
# Convert sha256_private_key string to decimal then hex.
hex_private_key = hex(int(sha256_private_key_str, 2))[2:]

binary_checksum = full264bit_24word_binary[-8:]

data_str = "\n".join(data_list)

# Clear terminal:
os.system('clear')

print(data_str)

print(f"\nConcatenated 4 digit decimals (x24):")
print(index_concat)

print(f"\n24 words as 264-bit binary - Last 8 bits ({binary_checksum}) are binary Checksum:")
print(full264bit_24word_binary)
# print(f"Last 8 bits ({binary_checksum}) are binary Checksum.")

print("\nRemove binary checksum to get 256-bit private key:")
print(sha256_private_key_str)

print("\nConvert to 64-digit hexadecimal:")
print(hex_private_key)

# word = 'smoke'
# index = bip39.WORDLIST.index(word)
# print(f"{word} : {index}")

'''
# 24 x 4 digit decimals (96):
040403510535204200720299055516110158048209901897061409531117132306701178201903450209010808140499

# 256 bits:
0011001010000101011111010000101111111111101000001001000001001010110100010101111001001011000100111100011110001001111011110111011010010100110011001110111001100010111011010010101101010011110100100110101111110001100101011001000110100010000110110001100101110001

# 264 bits (last appended 8 bits are part of checksum):
001100101000010101111101000010111111111110100000100100000100101011010001010111100100101100010011110001111000100111101111011101101001010011001100111011100110001011101101001010110101001111010010011010111111000110010101100100011010001000011011000110010111000111110011

32857d0bffa0904ad15e4b13c789ef7694ccee62ed2b53d26bf19591a21b1971
'''
