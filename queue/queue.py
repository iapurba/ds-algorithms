#!/usr/bin/env python3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = self.first

    def isEmpty(self):
        return self.first is None

    def peek(self):
        return self.first

    def enqueue(self, data):
        new_node = Node(data)
        if not self.first:
            self.first = new_node
            self.last = self.first
            return

        self.last.next = new_node
        self.last = new_node

    def dequeue(self):
        if not self.first: return

        if self.first is self.last:
            self.first = None
            self.last = self.first
            return

        temp = self.first
        self.first = temp.next
        temp = None

    def display(self):
        current = self.first
        if not current: return
        while current:
            print(f"|{str(current.data)}| -->", end=" ")
            current = current.next
        print()


if __name__ == "__main__":
    q = Queue()
    q.enqueue("Tom")
    q.enqueue("Sam")
    q.enqueue("Robin")
    q.dequeue()

    q.display()
