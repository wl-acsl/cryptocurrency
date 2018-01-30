import hashlib
import time

class Block:
    def __init__(self, index, timestamp, prev_hash, data):
        self.index = index
        self.block_hash = block_hash
        self.prev_hash = prev_hash
        self.merkle_root = merkle_root
        self.data = data

    def create_hash(self):
        return hashlib.sha256((str(index + timestamp + prev_hash + data)).encode('hex')).hexdigest()

def create_genesis():
    return Block(0, time.time(), "0", {"nonce": 1, "transactions": None})
