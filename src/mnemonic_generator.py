'''
cd ~/pypo && poetry shell
python src/mnemonic_generator.py

+-------------+--------------+--------------+-----------+---------------+
|Entropy Size |Entropy Bytes |Checksum Bits |Total Bits |Mnemonic Words |
+-------------+--------------+--------------+-----------+---------------+
|128 bits     |16 bytes      |4 bits        |132 bits   |12 words       |
|256 bits     |32 bytes      |8 bits        |164 bits   |24 words       |
+-------------+--------------+--------------+-----------+---------------+
'''

import tkinter as tk
from PIL import Image, ImageTk
from helpers.qr import QR

from embit import bip39
import hashlib
import random
import sys
import os
import time
# from make_qr_png import make_qr
# from pprint import pprint

# Clear terminal:
os.system('clear')

def keyboard_type(text, delay=0.01, end="\n"):
	for char in text:
		sys.stdout.write(char)
		sys.stdout.flush()
		# time.sleep(delay)
	if end:
		sys.stdout.write(end)
		sys.stdout.flush()

def create_checksum(bytes):
	"""Create a checksum of specified length. 256-bit (24 words): 8-bit checksum / 128-bit (12 words): 4-bit checksum."""
	'''
	INFO:
	Converts bytes[*] to SHA-256 hash "hashlib.sha256(bytes).digest()", represented as raw 32-byte binary object.
	Convert to a hexadecimal string "checksum_hex_str".
	Convert hex to 256-bit binary "checksum_bin".
	If supplied "bytes" arg is a 256-bit binary, return first 8 bits as the checksum.
	If supplied "bytes" arg is a 128-bit binary, return first 4 bits as the checksum.
	
	*128-bit binary represented as raw 16-byte binary object OR 256-bit binary represented as raw 32-byte binary object.
	
	Notes:
	hashlib.sha256(bytes).digest() -> A raw binary (bytes) object, containing the 256-bit (32-byte) SHA-256 hash.
	.hex() -> Converts the 32-byte hash into a 64 character hexadecimal string.
	'''
	checksum_hex_str = hashlib.sha256(bytes).digest().hex()
	checksum_bin = format(int(checksum_hex_str, 16), '0256b')
	# checksum_bin = bin(int(checksum_hex_str, 16))[2:].zfill(256)
	
	entropy_length = len(bytes) * 8
	checksum_length = entropy_length // 32
	
	return {
		"sha256_hash_hexadecimal": checksum_hex_str,
		"checksum": checksum_bin[:checksum_length],
	}

def generate_mnemonic(entropy_length):
	"""Generate mnemonic phrase based on specified entropy bits (128 or 256)."""
	# Nb. random.getrandbits(256) -> Python stores this internally in 256-bit binary format, but prints as a 77 digit decimal.
	# Convert the 256-bit or 128-bit to bytes.
	
	decimal = random.getrandbits(entropy_length)
	entropy_bytes = decimal.to_bytes(entropy_length // 8, byteorder='big')
	# entropy_bytes = random.getrandbits(entropy_length).to_bytes(entropy_length // 8, byteorder='big')
	entropy_bin = ''.join(f"{byte:08b}" for byte in entropy_bytes)
	result = create_checksum(entropy_bytes)
	checksum = result['checksum']
	binary_combined = entropy_bin + checksum
	segment_length = 11

	segments = [binary_combined[i:i+segment_length] for i in range(0, len(binary_combined), segment_length)]
	
	#DEBUG
	# print('entropy_length:', entropy_length)
	print('\ndecimal:', decimal)
	print('\nentropy_bin:', entropy_bin)
	print('\nentropy_bytes:', entropy_bytes)
	print('\nsegments:', segments)
	
	words = []
	dec_nos_str = ''
	bin_dec_word_list = []
	for segment in segments:
		dec_no = int(segment, 2)
		word = bip39.WORDLIST[dec_no]
		bin_dec_word_list.append(f"{segment} {dec_no:04} {word}")
		dec_nos_str += f"{dec_no:04}"
		words.append(word)
    
	return entropy_bin, checksum, segments, words, bin_dec_word_list, result['sha256_hash_hexadecimal'], dec_nos_str

'''
cable tribe fragile blame dove puppy prison bulk other hobby broom leave since into explain width crumble unusual enact attack front concert tissue tongue
'''
def data_from_mnemonic(words):
	entropy_bin = ''
	dec_nos_str = ''
	bin_dec_word_list = []
	segments = []
	
	for word in words:
		index = bip39.WORDLIST.index(word)
		segment = format(index, '011b') # dec -> 11-bit
		segments.append(segment)
		entropy_bin += segment
		bin_dec_word_list.append(f"{segment} {index:04} {word}")
		dec_nos_str += f"{index:04}"
	
	if 24 == len(words):
		# checksum = segment[-8:]
		entropy_bin = entropy_bin[:-8]
		entropy_length = 256
	elif 12 == len(words):
		# checksum = segment[-4:]
		entropy_bin = entropy_bin[:-4]
		entropy_length = 128
	
	dec_nos_int = int(entropy_bin, 2) # bin -> dec
	dec_nos_str = str(dec_nos_int)
	entropy_bytes = dec_nos_int.to_bytes(entropy_length // 8, byteorder='big')
	
	result = create_checksum(entropy_bytes)
	checksum = result['checksum']
	
	return entropy_bin, checksum, segments, words, bin_dec_word_list, result['sha256_hash_hexadecimal'], dec_nos_str
	
	# print(dec_nos_int)
	# print(entropy_bin)
	# print(entropy_bytes)
	# print(checksum)
	# sys.exit(1)


def make_bin_dec_word_table(bin_dec_word_list):
	hr = '+---------------+------------------+------------+'
	keyboard_type(hr, 0.01)
	keyboard_type('| 11-bit binary | 4-digit decimal  | BIP39 word |', 0.01)
	keyboard_type(hr, 0.01)
	for bin_dec_word in bin_dec_word_list:
		bin, dec, word = bin_dec_word.split()
		bin = f"{bin}".ljust(15)
		dec = f"{dec}".ljust(18)
		word = f"{word}".ljust(12)
		data = '|', bin, '|', dec, '|', word, '|'
		keyboard_type(data, 0.01)
	keyboard_type(hr, 0.01)

def also_int(str):
	try:
		int(str)
		return True
	except ValueError:
		return False

# User Selection: Generate 12 word mnemonic (128-bit entropy) or 24 word mnemonic (256-bit entropy)

input = input("Choose 12 word mnemonic (128-bit entropy) or 24 word mnemonic (256-bit entropy).\nEnter 12 or 24: ")
if '' == input:
	input = 24
else:
	if also_int(input):
		input = int(input.strip())
		if input not in [12, 24]:
			print("Invalid choice! Please enter 12 or 24.")
			sys.exit(1)
		else:
			# Convert input to entropy bits
			valid_values = {12: 128, 24: 256}
			entropy_length = valid_values[input]
			entropy_bin, checksum, segments, words, bin_dec_word_list, sha256_hash_hexadecimal, dec_nos_str = generate_mnemonic(entropy_length)
			
	elif 12 == len(input.split()) or 24 == len(input.split()):
		entropy_bin, checksum, segments, words, bin_dec_word_list, sha256_hash_hexadecimal, dec_nos_str = data_from_mnemonic(input.split())
		if 24 == len(input.split()):
			entropy_length = 256
		if 12 == len(input.split()):
			entropy_length = 128


keyboard_type(f"\nGenerated {entropy_length}-bit binary private key (entropy_bin): {entropy_bin}")
keyboard_type('\nCalculating the Checksum:')
keyboard_type(f"SHA-256 hash of private key: {sha256_hash_hexadecimal}\nNb. This hexadecimal hash is used as the checksum source.")

checksum_len = len(checksum)

if 4 == checksum_len:
	args = {"slice_len": 1, "bin_fmt": '04b'}
	print(f"\nFor 128-bit private keys (16 bytes) a {checksum_len}-bit checksum is required.")
elif 8 == checksum_len:
	args = {"slice_len": 2, "bin_fmt": '08b'}
	print(f"\nFor 256-bit private keys (32 bytes) an {checksum_len}-bit checksum is required.")

hex_slice = sha256_hash_hexadecimal[:args['slice_len']]
binary_representation = format(int(hex_slice, 16), args['bin_fmt'])

print(f"Convert the first hex digit to {checksum_len}-bit binary: {hex_slice} -> {binary_representation}")

keyboard_type(f"Checksum ({checksum_len}-bit): {checksum}")
keyboard_type("\nAppend the checksum to the private key, then split into 11-bit segments.\n")

make_bin_dec_word_table(bin_dec_word_list)

mnemonic_phrase = ' '.join(words)
print(f"\nMnemonic ({len(words)} word seed phrase):\n{mnemonic_phrase}")


data_list = [dec_nos_str]
qr = QR()
qr_images = [qr.qrimage(data) for data in data_list]
root = tk.Tk()
root.title("Seed Phrase QR")
label = tk.Label(root)
label.pack()

def update_qr_code(index=0):
    qr_image_tk = ImageTk.PhotoImage(qr_images[index])
    label.config(image=qr_image_tk)
    label.image = qr_image_tk
    root.update_idletasks()
    index = (index + 1) % len(qr_images)
    root.after(166, update_qr_code, index)

def quit_program(event):
    root.quit()

root.bind('q', quit_program)
root.bind('<Escape>', quit_program)
root.bind('<space>', quit_program)
update_qr_code()
root.mainloop()

# Nb. bin(decimal_77_digit) -> displays as 256-bit binary string (prefixed by '0b'). Doesn't display leading zeros.
#     format(decimal_77_digit, '0256b') -> displays as 256-bit binary string (no '0b' prefix). Pads with leading zeros to ensure 256-bit length.


'''
CHECKSUM NOTES:
4-bit checksums are required for 128-bit private keys.
4-bit checksums are a binary representation the first hex digit of the SHA-256 hash.

Example:
SHA-256 hash: 957baf5c048d24c7f6bf2c1cb3bf55883970fb8e1ffedc4b01ba1d9be5a1ee7b
First hex digit: 9 (binary representation: 1001)


8-bit checksums are required for 256-bit private keys.
8-bit checksums are a binary representation the first two hex digits of the SHA-256 hash.

Example:
SHA-256 hash: a46a3c3fd2bb204c4e196dc9a5ef0072c5bc159b850a8fc193830c8d036fe870
First two hex digits: a4 (binary representation: 10100100)
'''

'''
bytes = b'\x00\xae\x6f\x33\x44\x55\x66\x77\x88\x99\xaa\xbb\xcc\xdd\xee\xff'
bytes2hex = bytes.hex()
checksum = hashlib.sha256(bytes).digest()
'''
