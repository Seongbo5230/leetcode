from collections import defaultdict

class Solution:
    def shortestDistance(self, words, word1, word2): # return int
        dict = defaultdict(list)
        for index, word in enumerate(words):
            dict[word].append(index)

        loc1, loc2 = dict[word1], dict[word2]
        l1, l2 = 0, 0
        minDiff = float("inf")

        # print("Dict: ".format(dict))
        # print("loc1: {}, loc2: {}".format(loc1, loc2))
        # print("l1: {}, l2: {}, minDiff: {}".format(l1, l2, minDiff))
        # print("len(loc1): {}, len(loc2): {}\n\n".format(len(loc1), len(loc2)))

        while l1 < len(loc1) and l2 < len(loc2):
            minDiff = min(minDiff, abs(loc1[l1] - loc2[l2]))
            if loc1[l1] < loc2[l2]:
                l1 += 1
            else:
                l2 += 1
            # print("l1: {}, l2: {}, minDiff: {}".format(l1, l2, minDiff))

        return minDiff

    def shortestDistanceX(self, words, word1, word2): # return int
        l1 = l2 = -1
        minDiff = float("inf")
        for index, word in enumerate(words):
            if word1 == word:
                l1 = index
            elif word2 == word:
                l2 = index
            if l1 != -1 and l2 != -1:
                minDiff = min(minDiff, abs(l1 - l2))
        return minDiff

def main():
    words = ["practice", "makes", "perfect", "coding", "makes", "coding"]

    soln = Solution()
    answer = soln.shortestDistance(words, "practice", "coding")
    answer2 = soln.shortestDistanceX(words, "practice", "coding")
    print(answer)
    print(answer2)

if __name__ == "__main__":
    main()
