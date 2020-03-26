"""
Design a max stack that supports push, pop, top, peekMax and popMax.
https://leetcode.com/problems/max-stack/

push(x) -- Push element x onto stack.
pop() -- Remove the element on top of the stack and return it.
top() -- Get the element on the top.
peekMax() -- Retrieve the maximum element in the stack.
popMax() -- Retrieve the maximum element in the stack, and remove it. If you find more than one maximum elements, only remove the top-most one.
Example 1:
MaxStack stack = new MaxStack();
stack.push(5);
stack.push(1);
stack.push(5);
stack.top(); -> 5
stack.popMax(); -> 5
stack.top(); -> 1
stack.peekMax(); -> 5
stack.pop(); -> 1
stack.top(); -> 5
"""
class MaxStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack_q = []
        self.sorted_q = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack_q.append(x)
        if len(self.sorted_q) == 0 or  x >= self.sorted_q[-1]:
            self.sorted_q.append(x)

    def pop(self):
        """
        :rtype: int
        """
        ele=self.stack_q.pop()
        if ele == self.sorted_q[-1]:
            self.sorted_q.pop()
        return ele


    def top(self):
        """
        :rtype: int
        """
        return self.stack_q[-1]


    def peekMax(self):
        """
        :rtype: int
        """
        return self.sorted_q[-1]

    def popMax(self):
        """
        :rtype: int
        """
        max_ele = self.sorted_q.pop()
        tmp_stack = [] # store element of list before max_ele
        while self.stack_q[-1] != max_ele:
            tmp_stack.append(self.stack_q.pop())
        self.stack_q.pop()
        while len(tmp_stack) > 0:
            self.push(tmp_stack.pop())
        return max_ele


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()