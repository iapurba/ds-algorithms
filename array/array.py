#!/usr/bin/env python3

class Array:

    def __init__(self):
        self.data = {}
        self.lenght = 0


    def isEmpty(self):
        return self.lenght == 0


    def push(self, item):
        index = self.lenght
        self.data[index] = item
        self.lenght += 1


    def pop(self):
        item = self.data.pop(self.lenght-1)
        self.lenght -= 1
        return item


    def insert(self, index, item):
        if index < 0 or index > self.lenght: return

        if index == self.lenght:
            return self.push(item)

        for i in range(self.lenght, index, -1):
            self.data[i] = self.data[i-1]

        self.data[index] = item


    def remove(self, index):
        if index < 0 or index >= self.lenght: return

        if index == (self.lenght - 1):
            return self.pop()

        for i in range(index, self.lenght):
            self.data[i] = self.data[i+1]

        return self.pop()


if __name__ == "__main__":

    cars = Array()

    cars.push("bmw")
    cars.push("audi")
    cars.push("ford")
    cars.push("hundai")
    cars.push("jaguar")
    cars.push("tesla")
    cars.pop()
    cars.insert(2, "honda")
    cars.remove(3)

    print(cars.data)
