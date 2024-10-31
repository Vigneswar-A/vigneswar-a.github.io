class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        
        groups = set()
        
        for word in words:
            odd = []
            even = []
            for i, c in enumerate(word):
                if i%2:
                    odd.append(c)
                else:
                    even.append(c)
            odd.sort()
            even.sort()
            groups.add((tuple(odd), tuple(even)))
           
               
           
        
        return len(groups)
        
        
        