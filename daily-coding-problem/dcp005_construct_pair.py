#!/usr/bin/env python3

def cons(a, b):
    def pair(fn):
        return fn(a, b)
    return pair


def car(fn):
    def left(a, b):
        return a
    return fn(left)

  
def cdr(fn):
  def right(a, b):
    return b
  return fn(right)


if __name__ == "__main__":
    print(car(cons(2, 4)))
    print(cdr(cons(2, 4)))
