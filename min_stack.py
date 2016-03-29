"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
"""
class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_stack = []
        self.min_val_list = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.min_stack.append(x)
        if not self.min_val_list or x<=self.min_val_list[-1]:
            self.min_val_list.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        if self.min_stack[-1] == self.min_val_list[-1]:
            del self.min_val_list[-1]
        self.min_stack.pop()


    def top(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_val_list[-1]