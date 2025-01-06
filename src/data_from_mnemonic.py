'''
cd ~/pypo && poetry shell
python src/data_from_mnemonic.py

https://iancoleman.io/bip39

dry expose vocal shoe gesture point ignore rifle crumble injury inspire jaguar
"0541_0645_1962_1587_0779_1338_0902_1485_0422_0929_0938_0953"
"01000011101_01010000101_11110101010_11000110011_01100001011_10100111010_01110000110_10111001101_00110100110_01110100001_01110101010_01110111001"

entropy_bin: 01000011101010100001011111010101011000110011011000010111010011101001110000110101110011010011010011001110100001011101010100111011
checksum: 1001
segments: ['01000011101', '01010000101', '11110101010', '11000110011', '01100001011', '10100111010', '01110000110', '10111001101', '00110100110', '01110100001', '01110101010', '01110111001']
words: ['dry', 'expose', 'vocal', 'shoe', 'gesture', 'point', 'ignore', 'rifle', 'crumble', 'injury', 'inspire', 'jaguar']
bin_dec_word_list: ['01000011101 0541 dry', '01010000101 0645 expose', '11110101010 1962 vocal', '11000110011 1587 shoe', '01100001011 0779 gesture', '10100111010 1338 point', '01110000110 0902 ignore', '10111001101 1485 rifle', '00110100110 0422 crumble', '01110100001 0929 injury', '01110101010 0938 inspire', '01110111001 0953 jaguar']
sha256_hash_hexadecimal: 961cbb9b54eb037118f023bd8a8ccb41f978f0d0bca376df0b5883c9d4f3064a
dec_nos_str: 054106451962158707791338090214850422092909380953
'''

from embit import bip39
import hashlib
import os
import sys

os.system('clear')

from pprint import pprint
'''
while True:
	mnemonic_list = input('Enter 12 or 24 word seed phrase: ').split()
	mnemonic_len = len(mnemonic_list)
	if mnemonic_len not in [12, 24]:
		print('Incorrect number of words.')
	else:
		break
'''

# mnemonic_list = "dry expose vocal shoe gesture point ignore rifle crumble injury inspire jaguar".split()
# mnemonic_len = len(mnemonic_list)
# mnemonic_list = "endorse sea cook fault inherit recipe omit cheap nest plug doctor wonder song scare cash differ uncover better earn south neutral infant devote company".split()

def main_fnc(mnemonic):
	mnemonic_list = mnemonic.split()
	
	private_key_plus_checksum = ''
	word_indexes_pad0 = ''
	word_indexes_pad4 = ''
	for word in mnemonic_list:
		index = bip39.WORDLIST.index(word)
		binary_11_bit = format(index, '011b')
		private_key_plus_checksum += binary_11_bit
		dec_pad4 = f"{index:04}"
		word_indexes_pad0 += str(index)
		word_indexes_pad4 += dec_pad4
		# print(binary_11_bit, dec, word)

	mnemonic_len = len(mnemonic_list)
	checksum_size = int(mnemonic_len / 3)
	private_key = private_key_plus_checksum[:-checksum_size]
	
	binary_checksum_str, hex_str, private_key_bytes = calculate_checksum(private_key, mnemonic_len)
	
	
	return {
		"private_key": private_key,
		"private_key_plus_checksum": private_key_plus_checksum,
		"word_indexes_pad0": word_indexes_pad0,
		"word_indexes_pad4": word_indexes_pad4,
		"private_key_bytes": private_key_bytes,
		"mnemonic_len": mnemonic_len,
		"binary_checksum_str": binary_checksum_str,
		"hex_str": hex_str,
	}
# END: def main_fnc()


def calculate_checksum(private_key, mnemonic_len):
	entropy_length = len(private_key)
	private_key_bytes = int(private_key, 2).to_bytes(entropy_length // 8, byteorder='big')
	
	hex_str = hashlib.sha256(private_key_bytes).digest().hex()
	
	bit_size = int(mnemonic_len/3)
	binary_checksum_str = bin(int(hex_str[:int(bit_size/4)], 16))[2:].zfill(bit_size)
	
	return binary_checksum_str, hex_str, private_key_bytes


test_data = [
	{
		"mnemonic": "tuition success final north choice gold rate black eagle camp cluster opera",
		"word_indexes": "1873 1730 692 1202 321 802 1425 183 552 262 355 1242",
		"raw_binary": "11101010001 11011000010 01010110100 10010110010 00101000001 01100100010 10110010001 00010110111 01000101000 00100000110 00101100011 1001101",
		"binary_checksum": "1010",
	},
	{
		"mnemonic": "lawsuit field swallow garbage wreck elder pitch mountain eternal awful street bicycle permit town double journey lunch rare pitch gloom worry oblige device certain",
		"word_indexes": "1009 687 1752 764 2033 570 1324 1156 620 133 1719 175 1305 1842 525 963 1065 1424 1324 795 2030 1217 485 301",
		"raw_binary": "01111110001 01010101111 11011011000 01011111100 11111110001 01000111010 10100101100 10010000100 01001101100 00010000101 11010110111 00010101111 10100011001 11100110010 01000001101 01111000011 10000101001 10110010000 10100101100 01100011011 11111101110 10011000001 00111100101 001",
		"binary_checksum": "00101101",
	}
]

calc_data = [
	{
		"mnemonic": test_data[0]['mnemonic'], # reference mnemonic from test_data list.
		"word_indexes": main_fnc(test_data[0]['mnemonic'])['word_indexes_pad0'],
		"raw_binary": main_fnc(test_data[0]['mnemonic'])['private_key'],
		"binary_checksum": main_fnc(test_data[0]['mnemonic'])['binary_checksum_str'],
	},
	{
		"mnemonic": test_data[1]['mnemonic'],
		"word_indexes": main_fnc(test_data[1]['mnemonic'])['word_indexes_pad0'],
		"raw_binary": main_fnc(test_data[1]['mnemonic'])['private_key'],
		"binary_checksum": main_fnc(test_data[1]['mnemonic'])['binary_checksum_str'],
	}
]

def test_assert(args):
	test_data = args['test_data']
	calc_data = args['calc_data']
	
	keys = list(test_data[0].keys())
	
	tests = {
		"pass": 0,
		"fail": 0,
		"passed_test": [],
		"failed_test": [],
	}
	
	for i, _ in enumerate(test_data):
		try:
			for key in keys:
				if key != 'mnemonic':
					test_value = test_data[i][key]
					calc_value = calc_data[i][key]
					assert calc_value == test_value.replace(' ',''), f"failed ({key}) - got: {calc_value}"
			
			# Get 1st 3 mnemonic words
			mnemonic = ' '.join(test_data[i]['mnemonic'].split()[:3])+'...'
			
			tests['pass'] += 1
			tests['passed_test'].append(f"mnemonic test passed : {mnemonic}")
			
		except AssertionError as e:
			tests['fail'] += 1
			tests['failed_test'].append(str(e))
	
	if 0 == tests['fail']:
		print(f"All {tests['pass']} test(s) passed!")
		print('\n'.join(tests['passed_test']))
	elif tests['pass'] > 0:
		print(f"{tests['pass']} test(s) passed!")
		print('\n'.join(tests['passed_test']))

	if 0 == tests['pass']:
		print(f"All {tests['fail']} test(s) failed!")
		print('\n'.join(tests['failed_test']))
	elif tests['fail'] > 0:
		print(f"{tests['fail']} test(s) failed!")
		print('\n'.join(tests['failed_test']))
# END: def test_assert()

test_assert({
	'test_data': test_data,
	'calc_data': calc_data,
})
