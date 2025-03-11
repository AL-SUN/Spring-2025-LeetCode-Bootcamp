# my first python version
class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip() #whitespace 
        #signedness
        positivity  = True
        if s.startswith('-'):
            positivity = False
            s = s[1:]
        elif s.startswith('+'):
            s = s[1:]
        
        #conversion
        start = 0
        while start < len(s) and s[start] == '0':
            start += 1
            
        end = start
        while end < len(s) and s[end].isdigit():
            end += 1
        
        s = s[start:end]
        if len(s) == 0:
            return 0
        
        num = int(s)
        if not positivity:
            num = -num
        # rounding
        if num > 2**31 - 1:
            return 2**31 - 1
        elif num < -2**31:
            return -2**31
        else:
            return num
        
# Reflection: revise some string grammar in python, e.g. startswith, isdigit, strip, **, etc.


# A c++ version
# class Solution {
# public:
#     int myAtoi(string s) 
#     {
#         int i=0;
#         int sign=1;
#         long ans=0;
#         while(i<s.length() && s[i]==' ')
#             i++;
#         if(s[i]=='-')
#         {
#             sign=-1;
#             i++;
#         }
#         else if(s[i]=='+')
#             i++;
#         while(i<s.length())
#         {
#             if(s[i]>='0' && s[i]<='9')
#             {
#                 ans=ans*10+(s[i]-'0');
#                 if(ans>INT_MAX && sign==-1)
#                     return INT_MIN;
#                 else if(ans>INT_MAX && sign==1)
#                     return INT_MAX;
#                 i++;
#             }
#             else
#                 return ans*sign;
#         }
#         return (ans*sign);
#     }
# };

# Note: faster than the python version.
# Idea: revise some c++ grammar, e.g. INT_MAX, INT_MIN, etc.
# 1. multiple 10 to iterate each digit and char -'0' to get the digit.
# 2. use a long variable to store the result, and INT_MAX/INT_MIN to check the boundary condition. 