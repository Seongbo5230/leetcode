class Solution:
    def canPlaceFlowers(slef, flowerbed, n): # returns boolean
        plot = [0] + flowerbed + [0]
        index = 1
        while index < len(flowerbed) + 1 and n > 0:
            if plot[index - 1] == plot[index] == plot[index + 1]:
                n -= 1
                plot[index] = 1
            index += 1
        return n == 0

def main():
    soln = Solution()

    flowerbed = [1, 0, 0, 0, 1]
    fb = [1,0,0,0,1,0,0]
    one = soln.canPlaceFlowers(flowerbed, 1)
    two = soln.canPlaceFlowers(flowerbed, 2)
    three = soln.canPlaceFlowers(fb, 2)

    print(one)
    print(two)
    print(three)

if __name__ == "__main__":
    main()
