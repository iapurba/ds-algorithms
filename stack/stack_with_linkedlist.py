#!/usr/bin/env python3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top is None

    def peek(self):
        return self.top

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        return self

    def pop(self):
        if not self.top: return

        temp = self.top
        self.top = temp.next
        temp = None
        return self

    def printStack(self):
        current = self.top
        stack = []
        while current:
            stack.append(current.data)
            current = current.next
        print(stack[::-1])


if __name__ == "__main__":

    stack = Stack()

    stack.push('python')
    stack.push('java')
    stack.push('javascript')
    stack.push('ruby')
    stack.push('c++')
    stack.push('c#')
    stack.pop()
    stack.push('go')
    stack.pop()

    stack.printStack()
