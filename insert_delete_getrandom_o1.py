"""
380. Insert Delete GetRandom O(1)
https://leetcode.com/problems/insert-delete-getrandom-o1/
Design a data structure that supports all following operations in average O(1) time.

insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.
Example:

// Init an empty set.
RandomizedSet randomSet = new RandomizedSet();

// Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomSet.insert(1);

// Returns false as 2 does not exist in the set.
randomSet.remove(2);

// Inserts 2 to the set, returns true. Set now contains [1,2].
randomSet.insert(2);

// getRandom should return either 1 or 2 randomly.
randomSet.getRandom();

// Removes 1 from the set, returns true. Set now contains [2].
randomSet.remove(1);

// 2 was already in the set, so return false.
randomSet.insert(2);

// Since 2 is the only number in the set, getRandom always return 2.
randomSet.getRandom();
"""
from random import randint
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict_val = {}
        self.list_val = []


    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.dict_val:
            self.dict_val[val] = len(self.list_val)
            self.list_val.append(val)
            return True
        return False




    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.dict_val:
            list_index = self.dict_val[val]
            last_ele_index  = len(self.list_val) -1
            if list_index == last_ele_index:
                self.dict_val.pop(val)
                self.list_val.pop()
            else:
                self.dict_val[self.list_val[last_ele_index]] = list_index
                self.list_val[list_index], self.list_val[last_ele_index] =  self.list_val[last_ele_index], self.list_val[list_index]
                self.dict_val.pop(val)
                self.list_val.pop()
            # for index in range(list_index, len(self.list_val)):
            #     self.dict_val[self.list_val[index]] -= 1
            # self.dict_val.pop(val)
            # self.list_val.pop(list_index)
            return True
        else:
            return False


    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        random_index = randint(0, len(self.list_val)-1)
        return self.list_val[random_index]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()