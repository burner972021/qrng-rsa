import netsquid as ns
from netsquid.qubits import create_qubits, operate, measure
from netsquid.qubits.operators import H
from sympy import isprime

def qrng():
    qubit, = create_qubits(1)
    operate(qubit, H)
    result, _ = measure(qubit, observable=ns.Z)
    return result

def qrng_random_number(n_bits):
    bits = [qrng() for _ in range(n_bits)]
    return int(''.join(str(b) for b in bits), 2)

def getprime(n_bits=16):
    assert n_bits >= 2, "Bit length must be at least 2"
    while True:
        num = qrng_random_number(n_bits)
        num |= 1
        num |= (1 << (n_bits - 1))
        if isprime(num):
            return num

# example: generate 16 bit prime
prime = getprime(100)
print("Random 16-bit prime:", prime)
