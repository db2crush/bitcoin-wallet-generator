from bitcoin import *

############################ using python random function
# private_key = random_key()
# public_key = privtopub(private_key)
# wallet_address = pubtoaddr(public_key)

# print('private key: ', private_key)
# print('public key: ', public_key)
# print('bitcoin wallet address: ', wallet_address)
############################ using python random function

############################ using random 256 bits
bit_256 = '1011101101010110001000010001100100110000001000111101000010100011011001001101101111110110011010000011011010111010010100010110001001010001100100001100011100001100001101001010101011011010001001010001001110000101000110110001010010100011111010101001010110001111'
private_key = hex(int(bit_256, 2))[2:]
public_key = privtopub(private_key)
wallet_address = pubtoaddr(public_key)

print('private key: ', private_key)
print('public key: ', public_key)
print('bitcoin wallet address: ', wallet_address)

############################ using random 256 bits

