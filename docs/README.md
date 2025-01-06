# Required Files

[helpers/ur2/bytewords.py](https://github.com/daveswaves/seedsigner_seedqr/blob/master/src/helpers/ur2/bytewords.py) ([original](https://github.com/SeedSigner/seedsigner/blob/dev/src/seedsigner/helpers/ur2/bytewords.py))  
[helpers/ur2/cbor_lite.py](https://github.com/daveswaves/seedsigner_seedqr/blob/master/src/helpers/ur2/cbor_lite.py) ([original](https://github.com/SeedSigner/seedsigner/blob/dev/src/seedsigner/helpers/ur2/cbor_lite.py))  
[helpers/ur2/constants.py](https://github.com/daveswaves/seedsigner_seedqr/blob/master/src/helpers/ur2/constants.py) ([original](https://github.com/SeedSigner/seedsigner/blob/dev/src/seedsigner/helpers/ur2/constants.py))  
[helpers/ur2/crc32.py](https://github.com/daveswaves/seedsigner_seedqr/blob/master/src/helpers/ur2/crc32.py) ([original](https://github.com/SeedSigner/seedsigner/blob/dev/src/seedsigner/helpers/ur2/crc32.py))  
[helpers/ur2/fountain_decoder.py](https://github.com/daveswaves/seedsigner_seedqr/blob/master/src/helpers/ur2/fountain_decoder.py) ([original](https://github.com/SeedSigner/seedsigner/blob/dev/src/seedsigner/helpers/ur2/fountain_decoder.py))  
[helpers/ur2/fountain_encoder.py](https://github.com/daveswaves/seedsigner_seedqr/blob/master/src/helpers/ur2/fountain_encoder.py) ([original](https://github.com/SeedSigner/seedsigner/blob/dev/src/seedsigner/helpers/ur2/fountain_encoder.py))  
[helpers/ur2/fountain_utils.py](https://github.com/daveswaves/seedsigner_seedqr/blob/master/src/helpers/ur2/fountain_utils.py) ([original](https://github.com/SeedSigner/seedsigner/blob/dev/src/seedsigner/helpers/ur2/fountain_utils.py))  
[helpers/ur2/random_sampler.py](https://github.com/daveswaves/seedsigner_seedqr/blob/master/src/helpers/ur2/random_sampler.py) ([original](https://github.com/SeedSigner/seedsigner/blob/dev/src/seedsigner/helpers/ur2/random_sampler.py))  
[helpers/ur2/ur_decoder.py](https://github.com/daveswaves/seedsigner_seedqr/blob/master/src/helpers/ur2/ur_decoder.py) ([original](https://github.com/SeedSigner/seedsigner/blob/dev/src/seedsigner/helpers/ur2/ur_decoder.py))  
[helpers/ur2/ur_encoder.py](https://github.com/daveswaves/seedsigner_seedqr/blob/master/src/helpers/ur2/ur_encoder.py) ([original](https://github.com/SeedSigner/seedsigner/blob/dev/src/seedsigner/helpers/ur2/ur_encoder.py))  
[helpers/ur2/ur.py](https://github.com/daveswaves/seedsigner_seedqr/blob/master/src/helpers/ur2/ur.py) ([original](https://github.com/SeedSigner/seedsigner/blob/dev/src/seedsigner/helpers/ur2/ur.py))  
[helpers/ur2/utils.py](https://github.com/daveswaves/seedsigner_seedqr/blob/master/src/helpers/ur2/utils.py) ([original](https://github.com/SeedSigner/seedsigner/blob/dev/src/seedsigner/helpers/ur2/utils.py))  
[helpers/ur2/xoshiro256.py](https://github.com/daveswaves/seedsigner_seedqr/blob/master/src/helpers/ur2/xoshiro256.py) ([original](https://github.com/SeedSigner/seedsigner/blob/dev/src/seedsigner/helpers/ur2/xoshiro256.py))  

[helpers/embit_utils.py](https://github.com/daveswaves/seedsigner_seedqr/blob/master/src/helpers/embit_utils.py) ([original](https://github.com/SeedSigner/seedsigner/blob/dev/src/seedsigner/helpers/embit_utils.py))  
[helpers/qr.py](https://github.com/daveswaves/seedsigner_seedqr/blob/master/src/helpers/qr.py) ([original](https://github.com/SeedSigner/seedsigner/blob/dev/src/seedsigner/helpers/qr.py))

[models/decode_qr.py](https://github.com/daveswaves/seedsigner_seedqr/blob/master/src/models/decode_qr.py) ([original](https://github.com/SeedSigner/seedsigner/blob/dev/src/seedsigner/models/decode_qr.py))  
[models/encode_qr.py](https://github.com/daveswaves/seedsigner_seedqr/blob/master/src/models/encode_qr.py) ([original](https://github.com/SeedSigner/seedsigner/blob/dev/src/seedsigner/models/encode_qr.py))  
[models/qr_type.py](https://github.com/daveswaves/seedsigner_seedqr/blob/master/src/models/qr_type.py) ([original](https://github.com/SeedSigner/seedsigner/blob/dev/src/seedsigner/models/qr_type.py))  
[models/seed.py](https://github.com/daveswaves/seedsigner_seedqr/blob/master/src/models/seed.py) ([original](https://github.com/SeedSigner/seedsigner/blob/dev/src/seedsigner/models/seed.py))  
[models/settings_definition.py](https://github.com/daveswaves/seedsigner_seedqr/blob/master/src/models/settings_definition.py) ([original](https://github.com/SeedSigner/seedsigner/blob/dev/src/seedsigner/models/settings_definition.py))  

[test_seedqr.py](https://github.com/daveswaves/seedsigner_seedqr/blob/master/src/test_seedqr.py) ([original](https://github.com/SeedSigner/seedsigner/blob/dev/tests/test_seedqr.py))

## NOTES

BIP-32: Hierarchical Deterministic - derive public and private keys from a single master key (64 bytes). This allowed XPUBs and watch-only wallets.  
BIP-39: Mnemonic backup phrases (12 / 24 word seed phrase from a list of 2048 words)  
BIP-85: Deterministic Entropy (derive multiple seeds from one seed)  
BIP-174: PSBT spec
