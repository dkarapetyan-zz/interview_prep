# Design a stack that supports push, pop, top, and retrieving the minimum
# element in constant time.
#
# push(x)  Push element x onto stack.
# pop()  Removes the element on top of the stack.
# top()  Get the top element.
# getMin()  Retrieve the minimum element in the stack.
# Note that all the operations have to be constant time operations.
#
# Questions to ask the interviewer :
#
# Q: What should getMin() do on empty stack?
# A: In this case, return -1.
#
# Q: What should pop do on empty stack?
# A: In this case, nothing.
#
# Q: What should top() do on empty stack?
# A: In this case, return -1



class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    # @param x, an integer
    def push(self, x):
        self.stack.append(x)
        if len(self.min_stack) == 0:
            self.min_stack.append(x)
        else:
            self.min_stack.append(min(self.min_stack[-1], x))

    # @return nothing
    def pop(self):
        if len(self.stack) != 0:
            del self.stack[-1]
            del self.min_stack[-1]

    # @return an integer
    def top(self):
        if len(self.stack) != 0:
            return self.stack[-1]
        else:
            return -1

    # @return an integer
    def getMin(self):
        if len(self.min_stack) != 0:
            return self.min_stack[-1]
        else:
            return -1
