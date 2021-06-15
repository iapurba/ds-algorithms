#!/usr/bin/env python3

# Implementation of mean heap
class MinHeap:

    def __init__(self):
        self.heap = []
        self.size = 0

    # Inserting a value into the heap
    def insert(self, item):
        self.heap.append(item)
        self.size += 1
        self._heapify_up()

    # Peek the first item (min) from the heap
    def peek(self):
        if self.size == 0:
            return None
        return self.heap[0]

    # Removes the first as default
    # Removes a specific item of a given index if exists
    def remove(self, idx=0):
        size = self.size

        if idx > size:
            return

        self._swap(idx, size-1)
        self.heap.pop()
        self.size -= 1

        self._heapify_down(idx)

    # Helper function two swap items
    def _swap(self, idx1, idx2):
        heap = self.heap
        # Swaping items between two indices
        heap[idx1], heap[idx2] = heap[idx2], heap[idx1]

    # Helper function to heapify up
    def _heapify_up(self):
        idx = self.size - 1

        while (self._has_parent(idx) and self._parent(idx) > self.heap[idx]):
            self._swap(self._get_parent_idx(idx), idx)
            idx = self._get_parent_idx(idx)

     # Helper function to heapify down
    def _heapify_down(self, idx=0):

        while (self._has_left_child(idx)):
            smaller_child_idx = self._get_left_child_idx(idx)

            # If right child exists and less than the left child,
            # update the smaller child index to right child's index
            if (self._has_right_child(idx) and self._right_child(idx) < self._left_child(idx)):
                smaller_child_idx = self._get_right_child_idx(idx)

            # Swap if the parent is greater than the smaller child
            if self.heap[idx] > self.heap[smaller_child_idx]:
                self._swap(idx, smaller_child_idx)
            else:
                break

            # Update index to smaller child's index
            idx = smaller_child_idx

    # Helper function to get the left child's index
    def _get_left_child_idx(self, idx):
        return (2 * idx) + 1

    # Helper function to get the right child's index
    def _get_right_child_idx(self, idx):
        return (2 * idx) + 2

    # Helper function to get the parent's index
    def _get_parent_idx(self, idx):
        return (idx - 1) // 2

    # Helper function to check if an item has left child
    def _has_left_child(self, idx):
        return self._get_left_child_idx(idx) < self.size

    # Helper function to check if an item has right child
    def _has_right_child(self, idx):
        return self._get_right_child_idx(idx) < self.size

    # Helper function to check if an item has parent
    def _has_parent(self, idx):
        return self._get_parent_idx(idx) >= 0

    # Helper function to get the left child's value of a given index
    def _left_child(self, idx):
        if self._has_left_child(idx):
            return self.heap[self._get_left_child_idx(idx)]

    # Helper function to get the right child's value of a given index
    def _right_child(self, idx):
        if self._has_right_child(idx):
            return self.heap[self._get_right_child_idx(idx)]

    # Helper function to get the parent's value of a given index
    def _parent(self, idx):
        if self._has_parent(idx):
            return self.heap[self._get_parent_idx(idx)]


if __name__ == "__main__":

    mh = MinHeap()

    mh.insert(15)
    mh.insert(4)
    mh.insert(20)
    mh.insert(12)
    mh.insert(6)
    mh.insert(3)
    mh.insert(13)

    mh.remove()
    mh.remove(1)

    print(mh.heap)
