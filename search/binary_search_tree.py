# from collections import deque


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def depth_first_for_each(self, cb):
        # receives an anonymous function as a parameter. It should then execute
        # the anonymous function on each node in the tree in
        # [depth-first](https://en.wikipedia.org/wiki/Depth-first_search)
        # order. Your task is to implement the logic to traverse the tree in
        # depth-first pre-order fashion (as opposed to in-order or post-order).
        # Note that the pseudocode showcased on the Wikipedia article traverses
        # the tree in-order.
        # "Hint: you'll probably want to utilize a Stack data structure."
        cb(self.value)
        if self.left:
            self.left.depth_first_for_each(cb)
        if self.right:
            self.right.depth_first_for_each(cb)

    def breadth_first_for_each(self, cb):
        # receives a callback function as a parameter. It should then execute
        # the anonymous function on each node in the tree in
        # [breadth-first](https://en.wikipedia.org/wiki/Breadth-first_search)
        # order. Your task is to implement the logic to traverse the tree in
        # left-to-right breadth-first fashion.
        # "Hint: you'll probably want to utilize a Queue data structure."
        # bfs_queue = deque()
        pass

    def insert(self, value):
        new_tree = BinarySearchTree(value)
        if (value < self.value):
            if not self.left:
                self.left = new_tree
            else:
                self.left.insert(value)
        elif value >= self.value:
            if not self.right:
                self.right = new_tree
            else:
                self.right.insert(value)

    def contains(self, target):
        if self.value == target:
            return True
        if self.left:
            if self.left.contains(target):
                return True
        if self.right:
            if self.right.contains(target):
                return True
        return False

    def get_max(self):
        if not self:
            return None
        max_value = self.value
        current = self
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.right
        return max_value
