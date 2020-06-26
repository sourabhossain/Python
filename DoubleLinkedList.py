class Node:
    def __init__(self, value):
        self.next = None
        self.prev = None
        self.val = value


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        vals = []
        node = self.head

        while node is not None:
            vals.append(node.val)
            node = node.next
        return f"[{', '.join(str(val) for val in vals)}]"

    def pushFront(self, val):
        node = Node(val)

        if self.tail is None:
            self.head = node
            self.tail = node
            self.length += 1
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            self.length += 1

    def __remove_node(self, node):
        if node.prev is None:
            self.head = node.next
        else:
            node.prev.next = node.next

        if node.next is None:
            self.tail = node.prev
        else:
            node.next.prev = node.prev

    def remove(self, value):
        node = self.head

        while node is not None:
            if node.val == value:
                self.__remove_node(node)
            node = node.next

        self.length -= 1

    def popFront(self):
        if self.head is not None:
            self.__remove_node(self.head)
            self.length -= 1

    def popBack(self):
        if self.tail is not None:
            self.__remove_node(self.tail)
            self.length -= 1

    def reverse(self):
        node = None
        current = self.head

        while current is not None:
            node = current.prev
            current.prev = current.next
            current.next = node
            current = current.prev

        if node is not None:
            self.head = node.prev


my_list = DoubleLinkedList()

my_list.pushFront(10)
my_list.pushFront(20)
my_list.pushFront(30)
my_list.pushFront(40)
my_list.pushFront(50)

my_list.popFront()
my_list.reverse()

print(my_list)
print(f"length: {my_list.length}")
