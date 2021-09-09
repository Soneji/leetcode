'''
Results:
Runtime: 216 ms, faster than 14.46% of Python3 online submissions for Multiply Strings.
Memory Usage: 14.2 MB, less than 56.35% of Python3 online submissions for Multiply Strings.
'''

class Solution:

    def multiply(self, num1: str, num2: str) -> str:
        
        l1 = len(num1)
        l2 = len(num2)
        if l1 >= l2:
            num1, num2 = num2, num1
            l1, l2 = l2, l1
        
        total = 0
        for i in range(0, l2):
            for j in range(0, l1):
                zeroes = "0" * (l1 + l2 - j - i - 2)
                adder = int( str( int(num2[i]) * int(num1[j]) ) + zeroes )
                total += adder
        
        return str(total)
