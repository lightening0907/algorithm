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

class MinStack2(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack_q = []
        self.ordered_q = []


    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack_q.append(x)
        flag = 0
        for i in range(len(self.ordered_q)):
            if self.ordered_q[i]>=x:
                self.ordered_q.insert(i, x)
                flag = 1
                break
        if flag == 0:
            self.ordered_q.append(x)

    def pop(self):
        """
        :rtype: void
        """
        newest_ele = self.stack_q.pop()
        for i in range(len(self.ordered_q)):
            if self.ordered_q[i] == newest_ele:
                self.ordered_q.pop(i)
                break
        return newest_ele

    def top(self):
        """
        :rtype: int
        """
        return self.stack_q[-1]


    def getMin(self):
        """
        :rtype: int
        """
        return self.ordered_q[0]

minstack = MinStack2()
minstack.push(-2)
minstack.push(0)
minstack.push(-3)
print minstack.getMin()
print minstack.pop()
print minstack.top()
print minstack.getMin()
