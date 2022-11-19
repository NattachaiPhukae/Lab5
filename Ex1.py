class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def print_list(self):
        node = self.head
        while node is not None:
            print(node.data, end=' ')
            if node.next is not None:
                print('<->', end=' ')
            node = node.next
        print()


def main():
    dll = DoublyLinkedList()
    dll.insert(1)
    dll.insert(2)
    dll.insert(3)
    dll.insert(4)

    dll.print_list()


if __name__ == '__main__':
    main()