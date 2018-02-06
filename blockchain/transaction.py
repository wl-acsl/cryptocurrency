import base64
import ecdsa
import time

class Transaction:
    def __init__(self, inp, outp):
        self.inp = inp
        self.outp = outp

    def validate(self, public_key, signature, message):
        public_key = (base64.b64decode(public_key)).hex()
        signature = base64.b64decode(signature)
        vk = ecdsa.VerifyingKey.from_string(bytes.fromhex(public_key), curve=ecdsa.SECP256k1)

        try:
            return (vk.verify(signature, message.encode()))
        except:
            return False
    def sign(self, private_key):
        message = str(round(time.time()))
        bmessage = message.encode()
        sk = ecdsa.SigningKey.from_string(bytes.fromhex(private_key), curve=ecdsa.SECP256k1)
        signature = base64.b64encode(sk.sign(bmessage))

        return signature, message
