# Wrote three versions when solving the problem

class Solution1(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pre =[1]
        suf = [1]
        for i in range(len(nums)-1):
            pre.append(nums[i] * pre[i] )
            suf.append(nums[len(nums)-1 - i] * suf[i] )
        
        result = [pre[i]*suf[len(nums)-1-i] for i in range(len(nums))]

        return result
    
# Time Complexity: O(N), good 
# Space Complexity: O(N), but not good (excluding the final answer array)

# Solution: pre-compute the prefix and suffix 
# Idea: the core idea is to find the linear dependency in the problem and then use the dependency to solve the problem, since we want a linear time complexity solution.
# Note: division is not allowed, because we can't perform a division by 0.

class Solution2(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pre =[1]*len(nums)
        suf = [1]*len(nums)
        for i in range(len(nums)-1):
            pre[i+1] = nums[i] * pre[i] 
            suf[i+1] = nums[len(nums)-1 - i] * suf[i]
        
        result = [pre[i]*suf[len(nums)-1-i] for i in range(len(nums))]

        return result
    
# A space optimized version of the above solution. Use static arrays instead of dynamic arrays.


class Solution3(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pre =[1]*len(nums)
        suf = 1
        for i in range(len(nums)-1):
            pre[i+1] = pre[i] * nums[i] 

        for i in range(len(nums)-1, -1, -1):
            pre[i] *= suf
            suf *= nums[i] 

        return pre
    
# Time Complexity: O(N), good
# Space Complexity: O(1), good
# A space optimized version: the idea is that we don't actually need to seperately store intermediate product arrays, as we can directly store one into final answer array and use a variable to store the other.