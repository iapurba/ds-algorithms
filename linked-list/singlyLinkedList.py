#!/usr/bin/env python3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None


    # Insert at the beginning
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


    # Insert at the end
    def append(self, data):
        new_node = Node(data)
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node


    # Insert after a Node
    def insert(self, pos, data):
        if pos == 0:
            self.prepend(data)
            return

        leader = self._get_targeted_node(pos-1)

        if not leader: return

        new_node = Node(data)
        new_node.next = leader.next
        leader.next = new_node


    def remove(self, pos):
        if not self.head: return

        leader = self._get_targeted_node(pos-1)

        if pos == 0:
            self.head = leader.next
            leader = None
            return

        if not leader: return

        if not leader.next: return

        target = leader.next
        leader.next = target.next
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

    llist = SinglyLinkedList()
    llist.prepend(5)
    llist.prepend(12)
    llist.prepend(3)
    llist.prepend(10)
    llist.prepend(7)
    llist.append(20)
    llist.append(18)

    print("list:")
    llist.print_list()

    print("after inserting node:11 at index 5:")
    llist.insert(5, 11)
    llist.print_list()

    print("after removing node at index 3:")
    llist.remove(3)
    llist.print_list()
