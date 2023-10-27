from bitcoin import *
from mnemonic import Mnemonic

m = Mnemonic('english')

bit_256 = '1011101101010110001000010001100100110000001000111101000010100011011001001101101111110110011010000011011010111010010100010110001001010001100100001100011100001100001101001010101011011010001001010001001110000101000110110001010010100011111010101001010110001111'
entropy = hex(int(bit_256, 2))[2:]
print('entropy: ', entropy)
print('--------')

mnemonic_words = m.to_mnemonic(bytes.fromhex(entropy))
entropy_from_menemonic = bytearray.hex(m.to_entropy(mnemonic_words))
print('mnemonic_words: ', mnemonic_words)
print('entropy_from_menemonic: ', entropy)
print('--------')

priv = sha256(entropy)
priv_wif = encode_privkey(priv, 'wif')
priv_wif_c = encode_privkey(priv, 'wif_compressed')
print ('priv: ', priv)
print('priv_wif: ', priv_wif)
print('priv_wif_c', priv_wif_c)
print('--------')


pub = privtopub(priv)
pub_wif = privtopub(priv_wif)
pub_wif_c = privtopub(priv_wif_c)
print('pub: ', pub)
print('pub_wif', pub_wif)
print('pub_wif_c', pub_wif_c)
print('--------')

wallet_addr = pubtoaddr(pub)
wallet_addr_wif = pubtoaddr(pub_wif)
wallet_addr_wif_c = pubtoaddr(pub_wif_c)
print('wallet_addr', wallet_addr)
print('wallet_addr_wif', wallet_addr_wif)
print('wallet_addr_wif_c', wallet_addr_wif_c)