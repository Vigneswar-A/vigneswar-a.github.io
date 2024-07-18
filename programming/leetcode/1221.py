class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        hashmap=defaultdict(lambda :0)
        count=len(arr)//4+1
        
        for i in arr:
            hashmap[i]+=1
            if hashmap[i]>=count:
                return i
            
            

            
            
            
        