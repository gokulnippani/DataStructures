class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.set = set()

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):
        self.set.add(value)
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    # Your Solution Here
    if llist_1.size() == 0 and llist_2.size() == 0:
        print("No union. Empty lists")
        return
    if llist_1.size() == 0:
        return llist_2
    if llist_2.size() == 0:
        return llist_1

    set1 = llist_1.set
    set2 = llist_2.set
    unionlist = set()

    for key in set1:
        unionlist.add(key)
    for key in set2:
        unionlist.add(key)
    unionLinkedList = LinkedList()
    for key in unionlist:
        unionLinkedList.append(key)
    return unionLinkedList

def intersection(llist_1, llist_2):
    # Your Solution Here
    if llist_1.size() == 0 or llist_2.size() == 0:
        print("No intersection.")
        return
    set1 = llist_1.set
    set2 = llist_2.set
    intersection = set()
    interLinkedList = LinkedList()
    for key in set1:
        if key in set2:
            intersection.add(key)
    for key in intersection:
        interLinkedList.append(key)
    return interLinkedList


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))

# Test case 3

linked_list_4 = LinkedList()
linked_list_5 = LinkedList()

element_1 = []
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_4.append(i)

for i in element_2:
    linked_list_5.append(i)

print (union(linked_list_4,linked_list_5))
print (intersection(linked_list_4,linked_list_5))

# Test case 4

linked_list_6 = LinkedList()
linked_list_7 = LinkedList()

print (union(linked_list_6,linked_list_7))
print (intersection(linked_list_6,linked_list_7))