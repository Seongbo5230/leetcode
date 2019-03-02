class Solution:
    def maxSubArray(self, nums) -> int:
        if not nums:
            return 0
        curSum = maxSum = nums[0]

        for x in nums[1:]:
            curSum = max(x, curSum + x)
            # maxSum = max(maxSum, curSum)
            if curSum > maxSum:
                maxSum = curSum

        return maxSum

def main():
    list = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    soln = Solution()
    answer = soln.maxSubArray(list)
    print(answer)

if __name__ == "__main__":
    main()
