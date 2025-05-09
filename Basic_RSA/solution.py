from Crypto.Util.number import long_to_bytes, bytes_to_long, getPrime
from sympy import sqrt

cipher = 20757722207622037247635357492744031846725338097408869189520529130990427631410
n = 69114157160794333910763484211198332342669004707730845068021165933921964299353
m = 88316886119639368123247968201586633512
e = 65537

# m = p - q -> p = q + m
# n = p * q = (q + m) * q = q^2 + m * q
# -> q^2 + m * q - n = 0
# -> q = (-m ± sqrt(m² + 4n)) / 2
# -> p = q + m

disc = sqrt(m * m + 4 * n)
q = int((-m + disc) // 2)
p = int(q + m)

phi = (p - 1) * (q - 1)
d = pow(e, -1, phi)
plain = pow(cipher, d, n)

print(long_to_bytes(plain))