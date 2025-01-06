'''
cd ~/pypo && poetry shell
python src/decode_psbt_qr.py

https://github.com/SeedSigner/seedsigner/tree/0.6.0/src/seedsigner
https://github.com/SeedSigner/seedsigner/blob/0.6.0/tests/test_decodepsbtqr.py#L104

https://github.com/econoalchemist/SeedSigner
https://github.com/econoalchemist/econoalchemist.github.io/blob/main/interviews.md

'''

from models.seed import Seed
from models.decode_qr import DecodeQR, DecodeQRStatus
from models.qr_type import QRType
from models.psbt_parser import PSBTParser
from models.settings_definition import SettingsConstants
from embit import bip39
from embit.psbt import PSBT
from embit.descriptor import Descriptor

from pprint import pprint

def test_ur2_sparrow_singlesig_to_self():
	qrcodes = [
		"UR:CRYPTO-PSBT/435-3/LPCFADQDAXCFAOOECYMSTBHDCSHDVYHTAXLATPBEOEDPAYIAWSYNAMSGSARSURCLDRKNFYZEWLHLMDTNATNYNSETJNZOKBGLFMRTMWOTLAFSSTYNTIPTLTTLWPVOZEHTAHTESNYADSHYVYFPDEBTBAIHIYTLWFUERDLKWTLSNLMWCHNDPSBWGRUTKSYLFLATVDCYNTDNGDTNURYLTTGUSSHNAEEEFZSRLEKEHDEMCYOTLDEMOTZORFDPKBCLBEHNREFWIDOSRSLRIOIAOXNLADDYENFMVOGLSGECDKBECSDSLUHNDTWYYTWFSNSPPESAZCGUDLDABAISLNJLWKJPRHBBRTEHYALRJYNYKPEOGLGLOLCPPYSEZTCHVLFMPELDGWCXGMSPHPGWAOKNBALOFXJLKNONPRBAPKYKIEVETEDWFXMDRTVWBYKSZTBTCLSGCSCPIYTPTYGYKIYNRTJLHLIEMNJYCTVYUEHGPRHN",
		"UR:CRYPTO-PSBT/440-3/LPCFADROAXCFAOOECYMSTBHDCSHDVYAOAEAEAEAORTHKYLIDWSLTBGSGTBSNIHDMPKVSAAWYKNIACELDCMGRLULRKNLUMKRSBACNCPTBADAEAEAECNCPAECXJPRPLBLURFIHEMSWRFLNECGOTKGRMHLBCSAXTYJKREPKWEBWEYAYIYNDJPCWFSLSZCZMZMZMDLIHKNPYASHLWECEMEGSSSVTAEEEFZSRNSKEGSVYWNCMAMTNATMWCYMYWTUEPDTDAEAEAEAECNCPAECXONRSTTHSLBCPREBTRHBGJKSEWYPMTNPKEHIHHELPQDLSLPFRWNKBBTVAPMDTBEDAZCZMZMZMAOPKPEAOAEAEAEAEAECHPTBBCAWPEEVAOYIMDISSIDNNRFISRHBDGLATSASWAXGULTPDHSAEAEAEAEAEAECMAEBBJPRKBSISKTPSPLGRGSOEIYHDTLTTKIKORTJLHYVEMNKPCTAEDLFPBASG",
		"UR:CRYPTO-PSBT/441-3/LPCFADRHAXCFAOOECYMSTBHDCSHDVYHTAXLATPBEOEDPAYIAWSYNAMSGSARSURCLDRKNFYZEWLHLMDTNATNYNSETJNZOKBGLFMRTMWOTLAFSSTYNTIPTLTTLWPVOZEHTAHTESNYADSHYVYFPDEBTBAIHIYTLWFUERDLKWTLSNLMWCHNDPSBWGRUTKSYLFLATVDCYNTDNGDTNURYLTTGUSSHNAEEEFZSRLEKEHDEMCYOTLDEMOTZORFDPKBCLBEHNREFWIDOSRSLRIOIAOXNLADDYENFMVOGLSGECDKBECSDSLUHNDTWYYTWFSNSPPESAZCGUDLDABAISLNJLWKJPRHBBRTEHYALRJYNYKPEOGLGLOLCPPYSEZTCHVLFMPELDGWCXGMSPHPGWAOKNBALOFXJLKNONPRBAPKYKIEVETEDWFXMDRTVWBYKSZTBTCLSGCSCPIYTPTYGYKIYNRTJLHLIEMNJYCTVYWZGSVWDN",
		"UR:CRYPTO-PSBT/443-3/LPCFADRKAXCFAOOECYMSTBHDCSHDVYAXADCTPDIARTHKYLIDWSLTAASGSARSUECLSANEPDFZEHDLRNWSGLNNHTYTBNGRYLVYWDCPCLTDAEAEAEAEADDKAXTBCHOSVEHPAHTESNYAUYOYCKRNDRTBGWIHIYTLWFUERDNYWTMSLSROHKRPKELPLONDKOUEJSKBKGIHKNDNAYHLWENSMEGSSSHNAEEEFZSRNSKEGSVYWNEEAATAPYIMPASNHPFWMETEAYBYHFRSBBZCDSRDTTLNADLBEMFTTSSOAHENPFNTVSVEBDHNDTWYKBBDEYTSLPFRJSLBBTVADPDTBEDAKIZEZMZMAOPKPEAOAEAECPAOAXWKGRNLJEVSZMWSIDSOTTEHHETYFTFXCASBMKGTURBWJLIMTLLUFWSTSSKIZMLAFXBALUECZTFTHPISKTDWPEGRGSCPIYHDTLGYKIKORTJLHLVEMNKPCTAERKWPCMJN",
	]
	
	d = DecodeQR()
	
	for i in qrcodes:
		d.add_data(i)

	base64_psbt = d.get_base64_psbt()
	
	psbt = PSBT.from_string(base64_psbt)
	
	# only print outputs that are not change
	for out in psbt.outputs:
	    if not desc.owns(out):
	        print("Send %d to %s" % (out.value, out.script_pubkey.address()))
	    else:
	        print("Send %d (change) to %s" % (out.value, out.script_pubkey.address()))
	# print fee
	print("fee: %d" % base64_psbt.fee())

	# print(d.get_base64_psbt())
	# cHNidP8BAHECAAAAAQDo5ey+2HIrNUkExsFhsImv1OK1cYA9x/bRjYQD+0UaAQAAAAD9////AttBAAAAAAAAFgAUGixOLdCWw0YOKTZ5nH/nAFiHMmtAHwAAAAAAABYAFNbrl43uCJEN4CVjgbO9UzQYq3lB2XUfAE8BBDWHzwOUjfDCgAAAAIf4/x8q+YwsIsMjQZZKiYxG68KbV4Z0mlcxTbrtu8ApA/iB9364EPRoi0aEmjfRmywFry7wyW6Im2SQIsigPN9KEIshjoFUAACAAQAAgAAAAIAAAQDhAgAAAALAWfdi74cSytbNZS6q6ATuemMciRZLi4R6i5i/DiMi1gEAAAAjIgAgcrZ/i7xlN8a8hjVVz0uQfxgD1HO1qu0TMghmm3IbPYP9////L2V6qwld7RyRTMTgADRAw5x8TOHxFgbaB5Qaj/DeqNIAAAAAIyIAIKW/0WF/IrUNuRJzwe6t2qoxZV+Fs4OFO/F+DeatKRAl/f///wKqrwIAAAAAABepFB3sNOahaifEYp68aLkLTgfCxgNTh6hhAAAAAAAAFgAUcrsPaHesrktMomZY1dF9dsBvXuSOdR8AAQEfqGEAAAAAAAAWABRyuw9od6yuS0yiZljV0X12wG9e5AEDBAEAAAAiBgP2ZRGb0Lm2+j5nJyvr5Z3fGn7WJ60PMB2EsbA/LQ6etRiLIY6BVAAAgAEAAIAAAACAAAAAAAAAAAAAIgIDrP6rQqucOQEIEVa/N98mmnQ50B5IGGLEvCTDXAZJ0coYiyGOgVQAAIABAACAAAAAgAEAAAAAAAAAACICA+PijXYEywnDo/b1PUqGK6TA1kod1Ww5UiMjx8R9/4BDGIshjoFUAACAAQAAgAAAAIAAAAAAAwAAAAA=


	'''
	d = DecodeQR()
	
	for i in qrcodes:
		d.add_data(i)
		if d.qr_type == QRType.PSBT__UR2:
			print('1: True')
			print(d.qr_type)
	
	if d.is_complete:
		print('2: True')

	base64_psbt = "cHNidP8BAHECAAAAAQDo5ey+2HIrNUkExsFhsImv1OK1cYA9x/bRjYQD+0UaAQAAAAD9////AttBAAAAAAAAFgAUGixOLdCWw0YOKTZ5nH/nAFiHMmtAHwAAAAAAABYAFNbrl43uCJEN4CVjgbO9UzQYq3lB2XUfAE8BBDWHzwOUjfDCgAAAAIf4/x8q+YwsIsMjQZZKiYxG68KbV4Z0mlcxTbrtu8ApA/iB9364EPRoi0aEmjfRmywFry7wyW6Im2SQIsigPN9KEIshjoFUAACAAQAAgAAAAIAAAQDhAgAAAALAWfdi74cSytbNZS6q6ATuemMciRZLi4R6i5i/DiMi1gEAAAAjIgAgcrZ/i7xlN8a8hjVVz0uQfxgD1HO1qu0TMghmm3IbPYP9////L2V6qwld7RyRTMTgADRAw5x8TOHxFgbaB5Qaj/DeqNIAAAAAIyIAIKW/0WF/IrUNuRJzwe6t2qoxZV+Fs4OFO/F+DeatKRAl/f///wKqrwIAAAAAABepFB3sNOahaifEYp68aLkLTgfCxgNTh6hhAAAAAAAAFgAUcrsPaHesrktMomZY1dF9dsBvXuSOdR8AAQEfqGEAAAAAAAAWABRyuw9od6yuS0yiZljV0X12wG9e5AEDBAEAAAAiBgP2ZRGb0Lm2+j5nJyvr5Z3fGn7WJ60PMB2EsbA/LQ6etRiLIY6BVAAAgAEAAIAAAACAAAAAAAAAAAAAIgIDrP6rQqucOQEIEVa/N98mmnQ50B5IGGLEvCTDXAZJ0coYiyGOgVQAAIABAACAAAAAgAEAAAAAAAAAACICA+PijXYEywnDo/b1PUqGK6TA1kod1Ww5UiMjx8R9/4BDGIshjoFUAACAAQAAgAAAAIAAAAAAAwAAAAA="

	if base64_psbt == d.get_base64_psbt():
		print('3: True')

	tx = d.get_psbt()
	if str(tx) == d.get_base64_psbt():
		print('4: True')
	'''



test_ur2_sparrow_singlesig_to_self()