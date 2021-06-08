#!/usr/bin/env python3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = self.head


    # Insert at the beginning
    def prepend(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.tail = self.head
            return

        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node


    # Insert at the end
    def append(self, data):
        new_node = Node(data)

        if not self.tail:
            self.tail = new_node
            self.head = self.tail
            return

        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node


    # Insert after a Node
    def insert(self, pos, data):
        if pos == 0:
            self.prepend(data)
            return

        leader = self._get_targeted_node(pos-1)

        if not leader: return

        new_node = Node(data)
        new_node.next = leader.next
        leader.next.prev = new_node
        leader.next = new_node
        new_node.prev = leader


    def remove(self, pos):
        if not self.head: return

        leader = self._get_targeted_node(pos-1)

        if pos == 0:
            if self.head is self.tail:
                self.head = None
                self.tail = self.head
                return
            self.head = leader.next
            leader.next.prev = None
            leader = None
            return

        if not leader: return

        if not leader.next: return

        target = leader.next
        leader.next = target.next
        target.next.prev = leader
        target = None


    def print_list(self):
        current = self.head
        while current:
            print(f"|{str(current.data)}| -->", end=' ')
            current = current.next
        print()


    # Helper function to get the node in a given index
    def _get_targeted_node(self, pos):

        if not self.head: return

        current = self.head
        for i in range(pos):
            current = current.next
            if not current: return

        return current


if __name__ == "__main__":
    dllist = DoublyLinkedList()
    dllist.prepend(2)
    dllist.prepend(4)
    dllist.prepend(3)
    dllist.append(7)
    dllist.insert(2, 9)
    dllist.remove(0)

    dllist.print_list()
