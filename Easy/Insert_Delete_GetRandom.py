#Insert Delete GetRandom O(1)

#Implement the RandomizedSet class:

#RandomizedSet()
#   Initializes the RandomizedSet object.
#bool insert(int val)
#   Inserts an item val into the set if not present.
#   Returns true if the item was not present, false otherwise.
#bool remove(int val)
#   Removes an item val from the set if present.
#   Returns true if the item was present, false otherwise.
#int getRandom()
#   Returns a random element from the current set of elements
#   (it's guaranteed that at least one element exists when this method is called).
#   Each element must have the same probability of being returned.

#You must implement the functions of the class such that each function works in average O(1) time complexity.

import random as r

class RandomizedSet:

    def __init__(self):
        self.l = []

    def insert(self, val: int) -> bool:
        if val in self.l:
            return False
        self.l.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.l:
            return False
        self.l.remove(val)
        return True

    def getRandom(self) -> int:
        return self.l[r.randint(0, len(self.l) - 1)]

def main():
    ins = [["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"],
           [[], [1], [2], [2], [], [1], [2], []]]
    for i in range(len(ins[0])-1):
        obj = RandomizedSet()
        param_1 = obj.insert(ins[1])
        param_2 = obj.remove(ins[1])
        param_3 = obj.getRandom()

