"""
146. LRU Cache
https://leetcode.com/problems/lru-cache/

Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
"""

from collections import defaultdict
class LList(object):
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.child = None
        self.parent = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.root = None
        self.tail_key = None
        self.capacity = capacity
        self.LListmap = defaultdict(LList)
        self.depth = 0


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.LListmap:
            ele = self.LListmap[key].val
        else:
            return -1
        self.update_recency(key)
        return ele


    def update_recency(self, key):
        if self.LListmap[key].parent is not None:
            self.LListmap[key].parent.child = self.LListmap[key].child
            if self.LListmap[key].child is not None:
                self.LListmap[key].child.parent = self.LListmap[key].parent
            if key == self.tail_key:
                self.tail_key = self.LListmap[key].parent.key
            self.LListmap[key].child = self.root
            self.root.parent = self.LListmap[key]
            self.LListmap[key].parent = None
            self.root = self.LListmap[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if self.root is None:
            self.LListmap[key] = LList(key, value)
            self.root = self.LListmap[key]
            self.tail_key = key
            self.depth += 1
        else:
            if key in self.LListmap:
                self.LListmap[key].val = value
                self.update_recency(key)

            else:
                self.LListmap[key] = LList(key, value)
                self.LListmap[key].child = self.root
                self.root.parent = self.LListmap[key]
                self.root = self.LListmap[key]
                self.depth += 1
                if self.depth > self.capacity:
                    tmp = self.LListmap[self.tail_key].parent.key
                    del self.LListmap[self.tail_key]
                    self.tail_key = tmp
                    self.depth -= 1

lru_cache = LRUCache(2)
lru_cache.put(1, 1)
lru_cache.put(2, 2)
print(lru_cache.get(1))
lru_cache.put(3, 3)
print(lru_cache.get(2))
lru_cache.put(4, 4)
print(lru_cache.get(1))
print(lru_cache.get(3))
print(lru_cache.get(4))

