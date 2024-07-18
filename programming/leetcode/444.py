class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        graph={}
        n=len(nums)
        for i in range(1,n+1):
            graph[i]=set()
        for i in sequences:
            for j in range(len(i)-1):
                graph[i[j]].add(i[j+1])
        for i in range(n-1):
            if(nums[i+1] not in graph[nums[i]]):
                return False
        return True
                
        

                
        
        