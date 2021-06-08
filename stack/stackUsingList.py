#!/usr/bin/env python3

# Stack implementation using list
class Stack:
    def __init__(self):
        self.stack = []


    def isEmpty(self):
        return len(self.stack) == 0


    def push(self, data):
        self.stack.append(data)


    def pop(self):
        if not len(self.stack):
            print("Stack is empty")
            return
        return self.stack.pop()


    def peek(self):
        if not len(self.stack):
            print("Stack is empty")
            return
        return self.stack[-1]


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

    print(stack.stack)
