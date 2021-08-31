class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        index = 0
        minlen = 999999999999
        for i in range(len(strs)):
            if len(strs[i]) < minlen:
                minlen = len(strs[i])
                index = i
        
        shortest = strs.pop(index)
        count = 0
            
        for i in range(minlen):
            for string in strs:
                if string[i] != shortest[i]:
                    return shortest[0:count]
            count += 1

        return shortest[0:count]
