class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        if set(target).difference(set(source)):
            return -1
        
        n = len(source)
        j = 0
        for i in range(len(target)):
            while source[j%n] != target[i]:
                j += 1
            j += 1
        
        return ceil(j/n)
            
        