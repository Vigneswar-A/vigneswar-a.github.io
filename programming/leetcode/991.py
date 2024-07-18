class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        count=collections.Counter(arr)
        
        for i in sorted(arr,key=abs):
            if count[i]==0:continue
            if count[2*i]==0:
                return 0
            count[2*i]-=1
            count[i]-=1
            
        return 1