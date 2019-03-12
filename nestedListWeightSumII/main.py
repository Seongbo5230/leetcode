# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

from collections import defaultdict

class Solution:
    ####################
    # using cache/dict #
    ####################
    # def helperII(nestedList, level, cache):
    #     self.maxLevel = max(self.maxLevel, level)
    #
    #     for x in nestedList:
    #         if x.isInteger():
    #             cache[level] += x.getInteger()
    #         else:
    #             self.helperII(x.getList(), level + 1, cache)
    #     return

    # def depthSumInverse(self, nestedList):
    #     cache = defaultdict(int)
    #     self.maxLevel = -1
    #     self.helperII(nestedList, 1, cache)
    #
    #     totalSum = 0
    #
    #     for k, v in cache.items():
    #         totalSum = totalSum + v * (self.maxLevel - k + 1)
    #
    #     return totalSum

    #############
    # using BFS #
    #############
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int: #
        total, levelTotal = 0, 0
        level = nestedList

        while level:
            nextLevel = []
            for nestedInteger in level:
                if nestedInteger.isInteger():
                    levelTotal += nestedInteger.getInteger()
                else:
                    nextLevel.extend(nestedInteger.getList())
            total += levelTotal
            level = nextLevel

        return total

def main():
    # nestedList = [[1,1], 2, [1,1]]
    nestedList = [1, [4, [6]]]

    soln = Solution()
    # answer = soln.depthSum(nestedList)
    answer = soln.depthSumInverse(nestedList)
    print(answer)

if __name__ == "__main__":
    main()
