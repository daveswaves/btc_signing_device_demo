'''
cd ~/pypo && poetry shell
python src/hex_bin_dec.py 4

2^1  = 2
2^2  = 4
2^3  = 8
2^4  = 16
2^5  = 32
2^6  = 64
2^7  = 128
2^8  = 256
2^9  = 512
2^10 = 1024
2^11 = 2048
...
2^128 = 3.402823669×10³⁸
2^256 = 1.157920892×10⁷⁷
'''

import os
import sys

os.system('clear')

# bits equals 8 if no command-line argument, otherwise argument value
bits = int(sys.argv[1]) if len(sys.argv) == 2 else 8
bin_w = bits if bits > 8 else 8

if bits > 12:
	sys.exit('*** 12 BITS MAXIMUM ***')

dash_x = '-'*bin_w
space_x = ' '*(bin_w-5)

output = []
hr = f"+-----+--{dash_x}+---------+"
output.append(hr)
output.append(f"| hex | binary{space_x}| decimal |")
output.append(hr)
for i in range(2**bits): # 2^8 = 256
	hex_num = hex(i)[2:].upper().ljust(3) # [2:] to strip the 0x prefix
	bin_num = bin(i)[2:].ljust(bin_w) # [2:] to strip the 0b prefix
	dec_num = str(i).ljust(5)
	output.append(f"| {hex_num} | {bin_num} | {dec_num}   |")
output.append(hr)

print('\n'.join(output))
# print('\n'.join(output[::-1])) # reverse output
