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


class BlockChain:
    def __init__(self):
        self.HashChain = None

    def add_block(self, block : Block):
        if block is None:
            print('Invalid block.')
            return
        if self.HashChain is not None:
            block.previous_hash = self.HashChain[:-1]
        else:
            self.HashChain = ['0']

        self.HashChain.append(block.calc_hash())

    def __str__(self):
        if not self.HashChain:
            return "HashChain is empty."
        else:
            return '->'.join(self.HashChain[0:-1])

# tail = None
# for i in range(1, 5):
#     previous_hash = 0
#     if tail is not None:
#         previous_hash = tail.calc_hash()
#     current_node = Block(time.time(), str(i), previous_hash)
#
#     print(f"------------------------------- Block {i} Start -------------------------------")
#     print(f"Data - {i}")
#     print(f"Current Hash - {current_node.calc_hash()}")
#     print(f"Previous Hash - {current_node.previous_hash}")
#     print(f"Time - {current_node.timestamp}")
#     print(current_node.calc_hash())
#     print(f"-------------------------------  Block {i} End  -------------------------------")
#     tail = current_node
#     time.sleep(1)

print('----example 1----')
chain = BlockChain()
for i in range(1, 3):
    block = Block(time.time(), str(i), 0)
    chain.add_block(block)

print('Chain of Previous Hash.')
print(chain)

print('----example 2----')
chain = BlockChain()
print('Chain of Previous Hash.')
print(chain)

print('----example 3----')
chain = BlockChain()
for i in range(1, 2):
    block = Block(time.time(), str(i), 0)
    chain.add_block(block)

print('Chain of Previous Hash.')
print(chain)
