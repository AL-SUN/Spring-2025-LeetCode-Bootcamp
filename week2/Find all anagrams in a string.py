# my first version
import collections
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        anagrams = collections.Counter(p)
        start = 0 
        ans = []
        for i in range(len(s)):
            if start + len(p) > len(s): 
                break

            if s[i] not in anagrams:
                start = i + 1
                anagrams = collections.Counter(p) # tried to use copy.copy() but not efficient
            else:
                anagrams[s[i]] -= 1

                while anagrams[s[i]] < 0:
                    anagrams[s[start]] += 1
                    start += 1
                
                if i - start + 1 == len(p):
                    ans.append(start)
                    anagrams[s[start]] += 1
                    start += 1
        return ans    

# Idea: sliding window + hashmap
# a variation of substring problem --> sliding window
# store the frequency of each character --> hashmap

# Problem: have too many duplicate logic
# 1. no need to handle start when 'i - start + 1 == len(p)', as it can be included in 'while anagrams[s[i]] < 0'.
# 2. edge case 's[i] not in anagrams' alse can be handled by anagrams[s[i]] < 0.


# v2: improved logic and faster
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        anagrams = collections.defaultdict(int)
        for c in p:
            anagrams[c]+=1

        start = 0 
        ans = []
        for i, c in enumerate(s):
            if start + len(p) > len(s): 
                break

            anagrams[c] -= 1

            while anagrams[c] < 0:
                anagrams[s[start]] += 1
                start += 1
            
            if i - start + 1 == len(p):
                ans.append(start)
                
        return ans  

# Idea: defaultdict(int) to simplify the logic
# Revise python grammar: enumerate, defaultdict, etc.