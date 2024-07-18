class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        window = len(strs[0])
        
        for i in range(window , -1 , -1):
            curr = strs[0][:i]
            for string in strs:
                if not string.startswith(curr):
                    break
            else:
                return curr
        
        return ''
            
        