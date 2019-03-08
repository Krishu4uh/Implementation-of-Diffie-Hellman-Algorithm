# Implementation-of-Diffie-Hellman-Algorithm

DIFFIE HELLMAN ALGORITHM (DH)
Diffie Hellman (DH) key exchange algorithm is a method for securely exchanging cryptographic keys over a public
communications channel. Keys are not actually exchanged – they are jointly derived. It is named after their
inventors Whitfield Diffie and Martin Hellman.

If Alice and Bob wish to communicate with each other, they first agree between them a large prime number p,
and a generator (or base) g (where 0 < g < p).

Alice chooses a secret integer a (her private key) and then calculates g^a mod p (which is her public key).
Bob chooses his private key b, and calculates his public key in the same way.

Alice and Bob then send each other their public keys. Alice now knows a and Bob’s public key g^b mod p.
She is not able to calculate the value b from Bob’s public key as this is a hard mathematical problem
(known as the discrete logarithm problem). She can however calculate (g^b)^a mod p = g^ab mod p.

Bob knows b and g^a, so he can calculate (g^a)^b mod p = g^ab mod p. Therefore both Alice and Bob know
a shared secret g^ab mod p. An eavesdropper Eve who was listening in on the communication knows p, g,
Alice’s public key (g^a mod p) and Bob’s public key (g^b mod p). She is unable to calculate the shared
secret from these values.

In static-static mode, both Alice and Bob retain their private/public keys over multiple communications.
Therefore the resulting shared secret will be the same every time. In ephemeral-static mode one party will
generate a new private/public key every time, thus a new shared secret will be generated.
