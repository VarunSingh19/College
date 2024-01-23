class Solution:
    def __init__(self):
        self.memo = {}
    def rob(self, nums: list[int]) -> int:
        self.memo = {}
        return self.robFrom(0, nums)
    def robFrom(self, i:int, nums: list[int]) -> int:
        if i >= len(nums):
            return 0
        if i in self.memo:
            return self.memo[i]
        ans = max(self.robFrom(i + 1, nums), self.robFrom(i + 2, nums) + nums[i])
        self.memo[i] = ans
        
        return ans
    
# Example usage:
nums = [2, 7, 9, 3, 1]
solution = Solution()
result = solution.rob(nums)
print(result)