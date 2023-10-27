from bitcoin import *
from mnemonic import Mnemonic

# random 128bits entropy as hexadecimal characters
entropy = '6922ea35cea5879031de0524e444326f'

# initialize
m = Mnemonic('english')

# change entropy to mnemonic words
words = m.to_mnemonic(bytes.fromhex(entropy))

# change mnemonic words to entrpoy
entropy_from_words = bytearray.hex(m.to_entropy(words))

print('entropy: ', entropy)
print('entropy to mnemonic words: ', words)
print('entropy_from_words: ', entropy_from_words)