class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.myDict = {} # dictionary

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        # if the number to add is not in dictionary, then add to dict and increase count by 1 (starts at 0 by default)
        if number in self.myDict:
            self.myDict[number] += 1
        else:
            self.myDict[number] = 1

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        # find(value) and add(myDict[key1]) and add(myDict[key2])...
        # (value - key != key or self.myDict[key] > 1) is there to check just in case add(2), add(2) and then a find(4) case...
        for key in self.myDict:
            if value - key in self.myDict and (value - key != key or self.myDict[key] > 1):
                return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
