from collections import defaultdict


class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.cache = defaultdict()
        self.most_recent = DoublyLinkedList()
        self.max_capacity = capacity
        self.current_capacity = 0

    def get(self, key):
        if self.max_capacity == 0:
            print('Cache is disabled.')
            return
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key not in self.cache:
            return -1
        self.cache[key] = self.most_recent.update_least_used(self.cache[key])
        return self.cache[key].value.value


    def set(self, key, value):
        if self.max_capacity == 0:
            print('Cache is disabled.')
            return
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        # If Key is present check if values are equal. If not update the value.
        if key not in self.cache:
            curr_node = self.most_recent.append(NodeValue(key,value))
            self.cache[key] = curr_node
            self.current_capacity += 1
            if self.current_capacity >  self.max_capacity :
                self.cache.pop(self.most_recent.remove_head().key)
        else:
            if self.cache[key].value.value is not value:
                self.cache[key].value.value = value
            self.cache[key] = self.most_recent.update_least_used(self.cache[key])

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        if self.head is None:
            self.head = DoubleNode(value)
            self.tail = self.head
            return self.head

        self.tail.next = DoubleNode(value)
        self.tail.next.previous = self.tail
        self.tail = self.tail.next
        return self.tail

    def remove_head(self):
        if self.head is not None:
            curr_head = self.head
            self.head = curr_head.next
            self.head.previous = None
            curr_head.next = None
            return curr_head.value

    def update_least_used(self, current_node):
        if current_node.next is None:
            return current_node
        #If it's head
        if current_node.previous is None:
            self.head = current_node.next
            self.head.previous = None
        else:
            current_node.previous.next = current_node.next
            current_node.next.previous = current_node.previous

        current_node.next = None
        current_node.previous = self.tail
        self.tail.next = current_node
        self.tail = current_node
        return self.tail

class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class NodeValue:
    def __init__(self, key, value):
        self.key = key
        self.value = value


print("--------example 1 --------")
cache = LRU_Cache(2)

cache.set(2,1)
cache.set(1,1)
cache.set(2,3)
cache.set(4,1)
print(cache.get(1)) # -1
print(cache.get(2)) # 3

print("--------example 2 --------")

our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9) )     # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3) )     # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

print("--------example 3 --------")

our_cache = LRU_Cache(1)

our_cache.set(1, 1)
our_cache.set(2, 2)

print(our_cache.get(1))       # returns -1
print(our_cache.get(2))       # returns 2

print(our_cache.get(3) )     # returns -1

print("--------example 4 --------")
our_cache = LRU_Cache(0)
our_cache.set(1, 1)
# should display some appropriate warning message like "Can't perform operations on 0 capacity cache"
print(our_cache.get(1))
# should display some appropriate warning message like "Can't perform operations on 0 capacity cache"