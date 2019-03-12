from collections import defaultdict

class WordDistance:

    def __init__(self, words):
        self.locations = defaultdict(list)

        for index, word in enumerate(words):
            self.locations[word].append(index)

    def shortest(self, word1, word2):
        loc1, loc2 = self.locations[word1], self.locations[word2]
        l1, l2 = 0, 0
        minDiff = float("inf")

        while l1 < len(loc1) and l2 < len(loc2):
            minDiff = min(minDiff, abs(loc1[l1] - loc2[l2]))
            if loc1[l1] < loc2[l2]:
                l1 += 1
            else:
                l2 += 1
        return minDiff

def main():
    words = ["practice", "makes", "perfect", "coding", "makes", "coding"]

    soln = WordDistance(words)
    answer = soln.shortest("practice", "coding")
    print(answer)

if __name__ == "__main__":
    main()


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)
