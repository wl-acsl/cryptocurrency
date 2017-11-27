import ecdsa
import os
import hashlib
import base58

# Generate a keypair using ECDSA
private_key = os.urandom(32).encode('hex')
sign_key = ecdsa.SigningKey.from_string(private_key.decode('hex'), curve=ecdsa.SECP256k1)
verif_key = signing_key.verifying_key

public_key = ('\04'+verif_key.tostring()).encode('hex')

# Generate a wallet address
ripemd160 = hashlib.new('ripemd160')
ripemd160.update(hashlib.sha256(public_key.decode('hex')).digest())
middleman = '\00' + ripemd160.digest()
checksum = hashlib.sha256(hashlib.sha256(middleman).digest()).digest()[:4]

wallet_address = base58.b58encode(middleman + checksum)

# Handle connections and transactions -- to be filled in later
