from qrng import qrng_random_number
from Crypto.Util.number import bytes_to_long, long_to_bytes

message = b'this is a message'
m = bytes_to_long(message)
print("plaintext long :", m, " bit length :", m.bit_length())

# one time pad generation
otp = qrng_random_number(m.bit_length())

# keystream encryption
ciphertext = otp ^ m
print(ciphertext, long_to_bytes(ciphertext))

# decryption
m = ciphertext ^ otp
dec = long_to_bytes(m)
print("decrypted message: ", dec)