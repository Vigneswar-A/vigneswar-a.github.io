class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        temp = []
        for word in arr:
            if len(set(word)) != len(word):
                continue
            temp.append(word)

        arr = temp
        @cache
        def dp(idx=0, hashset=frozenset()):
            if idx == len(arr):
                return len(hashset)
            if not set(arr[idx])&hashset:
                return max(dp(idx+1, frozenset(set(arr[idx])|hashset)), dp(idx+1, hashset))
            return max(dp(idx+1, hashset), dp(idx+1))
        
        return dp()
                
        