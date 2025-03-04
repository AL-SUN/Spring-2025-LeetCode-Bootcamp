class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = p1 = 0
        p2 = len(nums) -1

        while i <= p2:
            if nums[i] == 0:
                nums[i] = nums[p1]
                nums[p1] = 0
                p1 += 1
                i += 1
            elif nums[i] == 2:
                nums[i] = nums[p2]
                nums[p2] = 2
                p2 -= 1
            else:
                i += 1

        return nums
            
# Solution: Three pointers/3-way partitioning/Dutch National Flag algorithm
# Idea: this is similar to sorting algorithms at first glance, but it's not because it only has 3 unique values. So a 3-way partitioning is enough. 
# Time Complexity: O(N), good
# Space Complexity: O(1), good


# A more elegant way to write the above solution:
class Solution(object):
    def sortColors(self, nums):
        low, mid, high = 0, 0, len(nums)-1
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

# Note: more readable variable names(low, mid, high), and python allows easier way of swapping two variables in one line.