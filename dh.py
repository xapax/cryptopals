"""
Publicly agreed mod and generator
These are publicly known by EVE


The two private keys must be large numbers, and the prime number used for MOD must be large
"""

# Mod/p must be a prime number and must be LARGEW
mod = 920419813
generator = 3
print "[*] Mod value: " + str(mod)
print "[*] Generator value: " + str(generator)


"""
These keys are private, and only known by alice and bob
"""

print "[*] Generating private keys"
# Generate LARGE keys
alice_private_key   = 100031
bob_private_key     = 133321

alice_calc = generator**alice_private_key % mod
bob_calc = generator**bob_private_key % mod


"""

Bob now sends his result (found in bob_calc) to alice
Alice sends her result (found in alice_calc) to bob
"""

print "[*] Blipblop over the wire bliblop exchaning reults blipblop"

"""
"""
# Alice performs this
secret_key = bob_calc**alice_private_key % mod 

# Bob performs this calculation
same_secret_key = alice_calc**bob_private_key % mod

print "[*] Secret key is produced, know by both parties: " + str(secret_key)
#print secret_key
#print same_secret_key

