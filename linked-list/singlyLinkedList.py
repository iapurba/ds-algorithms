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
    def insert(self, node, data):
        if not Node:
            print("The given previous node must be in the linkedList")
            return
        new_node = Node(data)
        new_node.next = node.next
        node.next = new_node


    def remove(self, pos):
        if not self.head: return

        leader = self.head

        if pos == 0:
            self.head = leader.next
            leader = None
            return

        for i in range(pos-1):
            leader = leader.next
            if leader is None:
                break

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

    print("after removing node at index 3:")
    llist.remove(3)
    llist.print_list()
