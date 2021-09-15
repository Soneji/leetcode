'''
Runtime: 36 ms, faster than 67.66% of Python3 online submissions for Generate Parentheses.
Memory Usage: 14.6 MB, less than 67.42% of Python3 online submissions for Generate Parentheses.
'''
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        self.backtrack(output, "", 0, 0, n)
        return output
        
    def backtrack(self, output, current, open, close, max):
        # base case
        if len(current) == max * 2:
            output.append(current)
            return
        
        if open < max:
            self.backtrack(output, current + "(", open + 1, close, max)
        
        if close < open:
            self.backtrack(output, current + ")", open, close + 1, max)
