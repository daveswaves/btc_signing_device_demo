'''
cd ~/pypo && poetry shell
python src/xpub2ur_standard.py
'''

import os
import sys
import tkinter as tk
from embit import bip39, bip32
from embit.networks import NETWORKS
from PIL import Image, ImageTk
from models.seed import Seed
from models.settings_definition import SettingsConstants
from helpers.qr import QR
from helpers.ur2.ur_encoder import UREncoder
from helpers.ur2.ur import UR

from urtypes.crypto import Account, HDKey, Output, Keypath, PathComponent, SCRIPT_EXPRESSION_TAG_MAP
from pprint import pprint

os.system('clear')
#'''
CONFIG = {
    "SEED_PHRASE_STR": "suffer lady fox order owner box next mammal federal embody vapor catalog solar text pen photo filter theme silent garment tip other improve true",
    "NETWORK": SettingsConstants.MAINNET,
    "DERIVATION": "m/84h/0h/0h", # equivalent
    "WORDLIST_LANGUAGE__ENGLISH": "en",
}

network: str = CONFIG['NETWORK']
wordlist_language_code: str = SettingsConstants.WORDLIST_LANGUAGE__ENGLISH

seed_phrase = CONFIG['SEED_PHRASE_STR'].split()

seed = Seed(mnemonic=seed_phrase, wordlist_language_code=wordlist_language_code)

root = bip32.HDKey.from_seed(seed.seed_bytes, version=NETWORKS[SettingsConstants.map_network_to_embit(network)]["xprv"])
fingerprint = root.child(0).fingerprint
xprv = root.derive(CONFIG['DERIVATION'])
xpub = xprv.to_public() # 'xpub6DG91CTsDWR8DokUUMfSXx9XpjH7UAgsqVT5nN3XnZDdQzeB1da4GrLhB1bkpp2FEq8mvkpLgGyNi8zqrVXH162i5f7XPnWVFtXfjRTKEpu'

print(f"Seed Phrase:\n{seed_phrase}")
print(f"\nXpub: {xpub}")

def derivation_to_keypath(path: str) -> list:
    arr = path.split("/")

    if arr[0] == "m":
        arr = arr[1:]
    
    for i, e in enumerate(arr):
        if e[-1] == "h" or e[-1] == "'":
            arr[i] = PathComponent(int(e[:-1]), True)
        else:
            arr[i] = PathComponent(int(e), False)

    return Keypath(arr, root.my_fingerprint, len(arr))

origin = derivation_to_keypath(CONFIG['DERIVATION'])

ur_hdkey = HDKey({
    'chain_code': xpub.chain_code,
    'key': xpub.key.serialize(),
    'origin': origin,
    'parent_fingerprint': xpub.fingerprint,
})

ur_outputs = []
if len(origin.components) > 0:
    if origin.components[0].index == 84: # Native Single Sig
        ur_outputs.append(Output([SCRIPT_EXPRESSION_TAG_MAP[404]], ur_hdkey))

ur_account = Account(root.my_fingerprint, ur_outputs)
qr_ur_bytes = UR("crypto-account", ur_account.to_cbor())
ur2_encode = UREncoder(ur=qr_ur_bytes, max_fragment_len=30)

data_list = []
loop_total = ur2_encode.fountain_encoder.seq_len()
for _ in range(loop_total):
    data = ur2_encode.next_part().upper()
    data_list.append(data)
#'''

'''
['UR:CRYPTO-ACCOUNT/1-4/LPADAACSJKCYZOVOWMDIHDCAOEADCYSFMYJTGDAOLYTAADMWTAADDLOXAXHDCLAXWECXETHHHHCXIMGAFSUYSAMUEE',
 'UR:CRYPTO-ACCOUNT/2-4/LPAOAACSJKCYZOVOWMDIHDCADPEEQDSERORHMEBBSWWSJPWDNEJLCXFRNEDSFPWNETEEEYAAHDCXLPKBKKMNDRIHSB',
 'UR:CRYPTO-ACCOUNT/3-4/LPAXAACSJKCYZOVOWMDIHDCACSBSBZMUNLDYYAONSOOYRFJOMOMOASSEZSPKIHGDSAGMWZKTYTKBGTZTLTYAWLLKHG',
 'UR:CRYPTO-ACCOUNT/4-4/LPAAAACSJKCYZOVOWMDIHDCAAMTAADDYOTADLNCSGHYKAEYKAEYKAOCYSFMYJTGDAXAXAYCYUYAASSRSAEHKRSASBA']
'''

'''
'Esc', 'Q' or spacebar to close QR-code
'''

# data_list = [
#     "UR:CRYPTO-PSBT/435-3/LPCFADQDAXCFAOOECYMSTBHDCSHDVYHTAXLATPBEOEDPAYIAWSYNAMSGSARSURCLDRKNFYZEWLHLMDTNATNYNSETJNZOKBGLFMRTMWOTLAFSSTYNTIPTLTTLWPVOZEHTAHTESNYADSHYVYFPDEBTBAIHIYTLWFUERDLKWTLSNLMWCHNDPSBWGRUTKSYLFLATVDCYNTDNGDTNURYLTTGUSSHNAEEEFZSRLEKEHDEMCYOTLDEMOTZORFDPKBCLBEHNREFWIDOSRSLRIOIAOXNLADDYENFMVOGLSGECDKBECSDSLUHNDTWYYTWFSNSPPESAZCGUDLDABAISLNJLWKJPRHBBRTEHYALRJYNYKPEOGLGLOLCPPYSEZTCHVLFMPELDGWCXGMSPHPGWAOKNBALOFXJLKNONPRBAPKYKIEVETEDWFXMDRTVWBYKSZTBTCLSGCSCPIYTPTYGYKIYNRTJLHLIEMNJYCTVYUEHGPRHN",
#     "UR:CRYPTO-PSBT/440-3/LPCFADROAXCFAOOECYMSTBHDCSHDVYAOAEAEAEAORTHKYLIDWSLTBGSGTBSNIHDMPKVSAAWYKNIACELDCMGRLULRKNLUMKRSBACNCPTBADAEAEAECNCPAECXJPRPLBLURFIHEMSWRFLNECGOTKGRMHLBCSAXTYJKREPKWEBWEYAYIYNDJPCWFSLSZCZMZMZMDLIHKNPYASHLWECEMEGSSSVTAEEEFZSRNSKEGSVYWNCMAMTNATMWCYMYWTUEPDTDAEAEAEAECNCPAECXONRSTTHSLBCPREBTRHBGJKSEWYPMTNPKEHIHHELPQDLSLPFRWNKBBTVAPMDTBEDAZCZMZMZMAOPKPEAOAEAEAEAEAECHPTBBCAWPEEVAOYIMDISSIDNNRFISRHBDGLATSASWAXGULTPDHSAEAEAEAEAEAECMAEBBJPRKBSISKTPSPLGRGSOEIYHDTLTTKIKORTJLHYVEMNKPCTAEDLFPBASG",
#     "UR:CRYPTO-PSBT/441-3/LPCFADRHAXCFAOOECYMSTBHDCSHDVYHTAXLATPBEOEDPAYIAWSYNAMSGSARSURCLDRKNFYZEWLHLMDTNATNYNSETJNZOKBGLFMRTMWOTLAFSSTYNTIPTLTTLWPVOZEHTAHTESNYADSHYVYFPDEBTBAIHIYTLWFUERDLKWTLSNLMWCHNDPSBWGRUTKSYLFLATVDCYNTDNGDTNURYLTTGUSSHNAEEEFZSRLEKEHDEMCYOTLDEMOTZORFDPKBCLBEHNREFWIDOSRSLRIOIAOXNLADDYENFMVOGLSGECDKBECSDSLUHNDTWYYTWFSNSPPESAZCGUDLDABAISLNJLWKJPRHBBRTEHYALRJYNYKPEOGLGLOLCPPYSEZTCHVLFMPELDGWCXGMSPHPGWAOKNBALOFXJLKNONPRBAPKYKIEVETEDWFXMDRTVWBYKSZTBTCLSGCSCPIYTPTYGYKIYNRTJLHLIEMNJYCTVYWZGSVWDN",
#     "UR:CRYPTO-PSBT/443-3/LPCFADRKAXCFAOOECYMSTBHDCSHDVYAXADCTPDIARTHKYLIDWSLTAASGSARSUECLSANEPDFZEHDLRNWSGLNNHTYTBNGRYLVYWDCPCLTDAEAEAEAEADDKAXTBCHOSVEHPAHTESNYAUYOYCKRNDRTBGWIHIYTLWFUERDNYWTMSLSROHKRPKELPLONDKOUEJSKBKGIHKNDNAYHLWENSMEGSSSHNAEEEFZSRNSKEGSVYWNEEAATAPYIMPASNHPFWMETEAYBYHFRSBBZCDSRDTTLNADLBEMFTTSSOAHENPFNTVSVEBDHNDTWYKBBDEYTSLPFRJSLBBTVADPDTBEDAKIZEZMZMAOPKPEAOAEAECPAOAXWKGRNLJEVSZMWSIDSOTTEHHETYFTFXCASBMKGTURBWJLIMTLLUFWSTSSKIZMLAFXBALUECZTFTHPISKTDWPEGRGSCPIYHDTLGYKIKORTJLHLVEMNKPCTAERKWPCMJN",
# ]


xpub_as_qr = input("\nExport Xpub as animated QR-code (y/n)? ")
try:
    xpub_as_qr
except NameError:
    xpub_as_qr = 'y'
if 'y' == xpub_as_qr:
    qr = QR()
    qr_images = [qr.qrimage(data) for data in data_list]
    root = tk.Tk()
    root.title("Xpub QR code")
    label = tk.Label(root)
    label.pack()

    def update_qr_code(index=0):
        qr_image_tk = ImageTk.PhotoImage(qr_images[index])
        label.config(image=qr_image_tk)
        label.image = qr_image_tk
        root.update_idletasks()
        index = (index + 1) % len(qr_images)
        root.after(166, update_qr_code, index)
        # root.after(1000, update_qr_code, index)

    def quit_program(event):
        root.quit()

    root.bind('q', quit_program)
    root.bind('<Escape>', quit_program)
    root.bind('<space>', quit_program)
    update_qr_code()
    root.mainloop()
