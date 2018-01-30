class NodeInfo:
    def __init__(self, addr, peers, wallet_addr):
        # hardcoded because it's easier
        self.addr = "localhost:3000"
        self.peers = ["localhost:3001", "localhost:3002", "localhost:3003"]
        self.wallet_addr = wallet_addr

class Node:
    # do stuff
