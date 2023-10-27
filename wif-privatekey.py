from bitcoin import *

wif_compressed = 'L2kTKR4A4Q1eizEsQGn1Efr6gTEEuxrHt3ibDXd1CzLzYRzM2KAv'

wallet_address_compressed = privtoaddr(wif_compressed)
print('wallet_address_compressed: ', wallet_address_compressed)

dec = decode_privkey(wif_compressed)
print('privkey as decimal: ', dec)

priv = hex(dec)[2:]
print('privkey', priv)
privtoaddr(priv)
wif = encode_privkey(priv,'wif')
print('wif', wif)
wif_compressed_from_privkey = encode_privkey(priv, 'wif_compressed')
print('wif_compressed_from_privkey', wif_compressed_from_privkey)

pubkey = privtopub(priv)
print('pubkey', pubkey)
pubkey_compresssed = privtopub(wif_compressed)
print('pubkey_compressed',pubkey_compresssed)