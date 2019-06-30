import hashlib
import time




class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()


    def calc_hash(self):
        sha = hashlib.sha256()

        hash_str = self.data.encode('utf-8')

        sha.update(hash_str)

        return sha.hexdigest()



tail = None
for i in range(1, 5):
    previous_hash = 0
    if tail is not None:
        previous_hash = tail.calc_hash()
    current_node = Block(time.time(), str(i), previous_hash)

    print(f"------------------------------- Block {i} Start -------------------------------")
    print(f"Data - {i}")
    print(f"Current Hash - {current_node.calc_hash()}")
    print(f"Previous Hash - {current_node.previous_hash}")
    print(f"Time - {current_node.timestamp}")
    print(current_node.calc_hash())
    print(f"-------------------------------  Block {i} End  -------------------------------")
    tail = current_node
    time.sleep(1)


