from Crypto.Util.number import bytes_to_long, long_to_bytes
from qrng import qrng, qrng_random_number, getprime

message = b'this is a message'
m = bytes_to_long(message)
print(m)

# initialise private keys and public keys
p, q = getprime(512), getprime(512)
n = p * q
print(n)
e = 0x10001

c = pow(m, e, n)
print(c)
print(long_to_bytes(c))

phi = (p-1) * (q-1)
d = pow(e, -1, phi)
dec = pow(c, d, n)
# check correctness
print(long_to_bytes(dec))