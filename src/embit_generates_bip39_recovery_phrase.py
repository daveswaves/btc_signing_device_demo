'''
cd ~/pypo && poetry shell
python src/embit_generates_bip39_recovery_phrase.py

# Module Installation
pip3 install embit

# Display installed Python modules:
pip3 list

# Check if specific module is installed:
pip3 show <MODULE> eg. pip3 show embit
'''


import os 
from embit import bip32, bip39
from embit.psbt import PSBT
from embit.descriptor import Descriptor
# binascii is part of the Python standard library - install not required.
from binascii import hexlify

os.system('clear')

# print(b"Hello, World!")
# print(hexlify(b"Hello, World!"))

'''
print("/**********************************************************************")
print(" Stepan Snigirev - Quantum physicist, bitcoin hacker (Munich, Germany).")
print(" https://github.com/diybitcoinhardware/embit/blob/master/docs/README.md")
print(" https://github.com/diybitcoinhardware/embit")
print(" https://embit.rocks/#/api/README")
print(" https://iancoleman.io/bip39/")
print("***********************************************************************/\n")
'''


# Generate mnemonic from 16 bytes of entropy (use real entropy here!):
mnemonic = bip39.mnemonic_from_bytes(b"128 bits is fine")
# >>> couple mushroom amount shadow nuclear define like common call crew fortune slice

# Generate root privkey, password can be omitted if you don't want it
seed = bip39.mnemonic_to_seed(mnemonic, password="my bip39 password")
root = bip32.HDKey.from_seed(seed)

# print('mnemonic:', mnemonic)
# print('seed:', seed)
# print('root:', root)

# Derive and convert to pubkey
xpub = root.derive("m/84h/0h/0h").to_public()
# print('xpub:', xpub)

# Generate native segwit descriptors.
# You can use {0,1} for combined receive and change descriptors
desc = Descriptor.from_string("wpkh([%s/84h/0h/0h]%s/{0,1}/*)" % (hexlify(root.my_fingerprint).decode(), xpub))
# >>> wpkh([67c32a74/84h/0h/0h]xpub6CH26VtYLqm5nw8UKA2qH8doMrvGZUpeQst1JkrmyGo9LYRoKVnyfgdvjcVQoK4XSWUwyZEcupk8wBh6a2mLJ82ouUo9x2n1Y3zeoEcRSYr/{0,1}/*)

'''
# Print first 5 addresses
for i in range(5):
    print(f'BTC address{i+1}:', desc.derive(i).address())
'''

'''

'''
# parse base64-encoded PSBT transaction
psbt = PSBT.from_string("cHNidP8BAHECAAAAAaW9Cd1X07XEcA/D0XmE5dwI2AEQr4aTTTwBqopD1mxAAAAAAAD9////AvJJXQUAAAAAFgAUUa2Cs4u5XOmDFhwNxl/szK5L9beAlpgAAAAAABYAFCwSoUTerJLG437IpfbWF8DgWx6kAAAAAAABAHECAAAAATVenbXof59P6l5N+BxpXQytbyWp29JfJDyT+OwohRWKAAAAAAD+////AgDh9QUAAAAAFgAUgmkBPePxvl4jTWsuNNnypKngm824IKMwAAAAABYAFOiPQIZGLU3UZ8JugMpHcCwxmUK2zQEAAAEBHwDh9QUAAAAAFgAUgmkBPePxvl4jTWsuNNnypKngm80iBgPHS/KrcrFXnxQ0/kvZeBkmEsQGjBLEc5JRUjzP9yVXVhhnwyp0VAAAgAAAAIAAAACAAAAAAAAAAAAAIgIC9jzRiRyPDoZ5F2xMV/QfW6qma/6i0PtyELYn8YR5PjsYZ8MqdFQAAIAAAACAAAAAgAEAAAAAAAAAAAA=")

print(dir(psbt)) # -> <function PSBT.to_string at 0x70fa6ed58d30>

# for inp in psbt.inputs:
#     if inp.utxo:
#         print("Previous TxID:", inp.utxo.txid.hex())
#         print("Output Index:", inp.utxo.index)
#     elif inp.non_witness_utxo:
#         print("Previous TxID:", inp.non_witness_utxo.txid.hex())
#         print("Output Index:", inp.index)
#     else:
#         print("UTXO information is missing for this input.")
    
    # print("TxID:", inp.prev_txid.hex())
    # print("Output Index:", inp.prev_index)
    # if inp.witness_utxo:
    #     print("Amount (satoshis):", inp.witness_utxo.value)
    #     print("ScriptPubKey:", inp.witness_utxo.script_pubkey)

'''
# only print outputs that are not change
for out in psbt.outputs:
    if not desc.owns(out):
        print("Send %d to %s" % (out.value, out.script_pubkey.address()))
    else:
        print("Send %d (change) to %s" % (out.value, out.script_pubkey.address()))
# print fee
print("fee: %d" % psbt.fee())
'''

# sign psbt and print it
psbt.sign_with(root)
# print('PSBT:', psbt)
# print('PSBT (signed):', psbt)
