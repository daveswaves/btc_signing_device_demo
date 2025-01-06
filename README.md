A collection of python scripts to explore some of the operations of the SeedSigner signing device.

## Setup

Extract following libraries:
```
helpers.7z
models.7z
urtypes.7z
```

The `pyproject.toml` file uses Poetry to install the required dependencies for the project.

When the virtual environment is running, run `$ pip list` to view all the project packages.

Alternatively, `$ pip show <PACKAGE>` to view package details.

## src/bip39.py

Converts a 24 word mnemonic into its component decimal/binary representation and tabulates the results.

Eg: crater cloud drill young animal century earth siren because detail knock unfold error jaguar merry pistol fatigue nation wise clinic boss assault grape dinosaur

```javascript
+---------+---------+------------+
| Word    | Decimal | Binary     |
+---------+---------+------------+
|crater   |0404     |00110010100 |
|cloud    |0351     |00101011111 |
|drill    |0535     |01000010111 |
|young    |2042     |11111111010 |
|animal   |0072     |00001001000 |
|century  |0299     |00100101011 |
|earth    |0555     |01000101011 |
|siren    |1611     |11001001011 |
|because  |0158     |00010011110 |
|detail   |0482     |00111100010 |
|knock    |0990     |01111011110 |
|unfold   |1897     |11101101001 |
|error    |0614     |01001100110 |
|jaguar   |0953     |01110111001 |
|merry    |1117     |10001011101 |
|pistol   |1323     |10100101011 |
|fatigue  |0670     |01010011110 |
|nation   |1178     |10010011010 |
|wise     |2019     |11111100011 |
|clinic   |0345     |00101011001 |
|boss     |0209     |00011010001 |
|assault  |0108     |00001101100 |
|grape    |0814     |01100101110 |
|dinosaur |0499     |00111110011 |
+---------+---------+------------+

Concatenated 4 digit decimals (x24):
040403510535204200720299055516110158048209901897061409531117132306701178201903450209010808140499

24 words (264-bit binary) - Last 8 bits (11110011) is the binary Checksum:
001100101000010101111101000010111111111110100000100100000100101011010001010111100100101100010011110001111000100111101111011101101001010011001100111011100110001011101101001010110101001111010010011010111111000110010101100100011010001000011011000110010111000111110011

Remove binary checksum to get 256-bit private key:
0011001010000101011111010000101111111111101000001001000001001010110100010101111001001011000100111100011110001001111011110111011010010100110011001110111001100010111011010010101101010011110100100110101111110001100101011001000110100010000110110001100101110001

Convert the 256-bit binary to 64-digit hexadecimal:
32857d0bffa0904ad15e4b13c789ef7694ccee62ed2b53d26bf19591a21b1971
```