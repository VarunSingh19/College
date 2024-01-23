class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        sub = [nums[0]]
        
        for num in nums[1:]:
            if num > sub[-1]:
                sub.append(num)
            else:
                i = 0
                while num > sub[i]:
                    i += 1
                sub[i] = num
        print(sub)
        return len(sub)
    
#  Example usage:
nums = [10, 9, 2, 5, 3, 7, 101, 18]
solution = Solution()
result = solution.lengthOfLIS(nums)
print(result)