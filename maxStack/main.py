class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.maxStack = [] # use a 2nd stack to keep track of max value

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.maxStack: # for first iteration when maxStack is empty
            self.maxStack.append(x)
        else:
            self.maxStack.append(max(x, self.maxStack[-1])) # push to maxStack if value increases

    def pop(self) -> int:
        self.maxStack.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        return self.maxStack[-1]

    def popMax(self) -> int:
        maxStackItem = self.maxStack.pop() # need to find this in our stack
        tempStack = []

        while self.stack[-1] != maxStackItem:
            tempStack.append(self.pop())

        retItem = self.stack.pop()

        for i in range(len(tempStack) - 1, -1, -1):
            self.push(tempStack[i])
            # self.stack.append(tempStack.pop())

        return retItem

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()

# # Hardest part of this question is figuring out an efficient was to pop max.
# # I originally was trying to do something similar to LFU cache with double linked lists,
# # but couldn't figure out how to save the sequential maxes after popping the max.
# # So right now I take the brute force approach of popping everything out from both stacks
# # until we reach the max, and add the elements that were previously popped, back in.
# class MaxStack(object):
#
#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.stack = []
#         self.maxHeap = []
#         self.toPop_heap = {} #to keep track of things to remove from the heap
#         self.toPop_stack = set() #to keep track of things to remove from the stack
#
#     def push(self, x):
#         """
#         :type x: int
#         :rtype: void
#         """
#         heapq.heappush(self.maxHeap, (-x,-len(self.stack)))
#         self.stack.append(x)
#
#     def pop(self):
#         """
#         :rtype: int
#         """
#         self.top()
#         x = self.stack.pop()
#         key = (-x,-len(self.stack))
#         self.toPop_heap[key] = self.toPop_heap.get(key,0) + 1
#         return x
#
#     def top(self):
#         """
#         :rtype: int
#         """
#         while self.stack and len(self.stack)-1 in self.toPop_stack:
#             x = self.stack.pop()
#             self.toPop_stack.remove(len(self.stack))
#         return self.stack[-1]
#
#     def peekMax(self):
#         """
#         :rtype: int
#         """
#         while self.maxHeap and self.toPop_heap.get(self.maxHeap[0],0):
#             x = heapq.heappop(self.maxHeap)
#             self.toPop_heap[x] -= 1
#         return -self.maxHeap[0][0]
#
#     def popMax(self):
#         """
#         :rtype: int
#         """
#         self.peekMax()
#         x,idx = heapq.heappop(self.maxHeap)
#         x,idx = -x,-idx
#         self.toPop_stack.add(idx)
#         return x

# print("")
# print("".format())
def main():
    stack = MaxStack()
    stack.push(5)
    print("Pushed 5")
    stack.push(1)
    print("Pushed 1")
    print("Popped Max: {}".format(stack.popMax()))
    # print("Top: {}".format(stack.top()))
    print("Peek Max: {}".format(stack.peekMax()))

if __name__ == "__main__":
    main()
