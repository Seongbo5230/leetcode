class Solution:
    def productExceptSelf(self, nums):
        product = 1
        output = []

        for x in range(len(nums)):
            output.append(product)
            product *= nums[x]
        product = 1 # reset product value
        for x in range(len(nums) - 1, -1, -1):
            output[x] *= product
            product *= nums[x]

        return output

def main():
    nums = [2, 3, 4, 5]
    soln = Solution()
    answer = soln.productExceptSelf(nums)
    print(answer)

if __name__ == "__main__":
    main()
