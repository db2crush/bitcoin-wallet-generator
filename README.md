## bitcoin-wallet-generator
Bitcoin wallet generator with python

## install python
https://www.python.org/downloads/

## install bitcoin lib
```
pip install bitcoin
```

## concepts
```
(entropy <-> mnemonics) -> (WIF <-> private key) -> public key -> wallet address

entropy 128bits -> mnemonics


1bit = 0 / 1
1byte = 8 bits
SHA256 = 256 bits, 256/8=32 bytes
1Hexadecimal character= 4bits

256bits=32bytes=64hexadecimal characters
```

## WIF
```
WIF = wallet import format
WIF_C = wallet import format compressed, commonly used

Private Key WIF
51 characters base58, starts with a '5'

Private Key WIF Compressed
52 characters base58, starts with a 'K' or 'L'

```

## refer
```
bitaddress.org
```