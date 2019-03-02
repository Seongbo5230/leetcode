# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals):
        intervals.sort(key = lambda x: x.start)
        merged = []

        for interval in intervals:
            if not merged or merged[-1].end < interval.start: # very first or normal operation
                merged.append(interval)
            else: # there is an overlap
                merged[-1].end = max(merged[-1].end, interval.end)

        return merged

def main():
    i1 = Interval(1,3)
    i2 = Interval(2,6)
    i3 = Interval(8,10)
    i4 = Interval(15,18)
    intervals = [i1, i2, i3, i4]
    soln = Solution()
    answer = soln.merge(intervals)

    # for x in answer:
    #     print("{} {}".format(x.start, x.end))

if __name__ == "__main__":
    main()
