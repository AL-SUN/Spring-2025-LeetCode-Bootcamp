class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        p1= 0
        p2 = len(numbers) - 1

        while p1<p2:
            sum = numbers[p1] + numbers[p2]  
            if sum == target:
                return [p1+1, p2+1]
            elif sum > target:
                p2-=1
            else:
                p1+=1
        
        return []
    
# Solution: Two pointers, one at the start and one at the end of the list.
# Idea: the core idea is that the input list is sorted, so we can ensure that linear search will work.
# Time Complexity: O(N)
# Space Complexity: O(1)