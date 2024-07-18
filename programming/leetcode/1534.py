class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        counts = {'c':0 , 'r':0 , 'o':0 , 'a':0 , 'k':0}
        max_crocks = 0
        order = {'c':'c' , 'r':'c' , 'o':'r' , 'a':'o' , 'k':'o'}
        
        for c in croakOfFrogs:
            counts[c] += 1
            if counts[order[c]] < counts[c]:
                return -1
            if c == 'k':
                for letter in counts:
                    counts[letter] -= 1
            max_crocks = max(counts['c'] , max_crocks)
            
        return max_crocks if counts['c'] == counts['k'] else -1
            
        