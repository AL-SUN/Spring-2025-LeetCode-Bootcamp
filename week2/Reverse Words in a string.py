# v1: inbuilt functions
# Time: O(n)
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.strip().split()
        words.reverse()
        return " ".join(words)
    
# v2: two pointers
# Time: O(n)
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = []
        l = len(s)-1
        for r in range(len(s)-1, -1 ,-1):
            if s[r] == ' ':
                if s[l].isalnum():
                    words.append(s[r+1:l+1])
                    l = r
            else:
                if s[l] == ' ':
                    l = r
        # last
        if s[l].isalnum():
            words.append(s[0:l+1])

        return " ".join(words)

            