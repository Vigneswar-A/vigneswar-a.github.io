class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashmapu = {}
        hashmapv = {}
        
        for u,v in zip(s , t):
            if (u in hashmapu) != (v in hashmapv):
                return False
            
            elif u not in hashmapu:
                hashmapu[u] = v
                hashmapv[v] = u
                
            elif hashmapu[u] != v or hashmapv[v] != u:
                return False

        return True
        