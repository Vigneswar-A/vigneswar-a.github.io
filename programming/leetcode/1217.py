class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        hashmap=dict((i,j) for j,i in enumerate(arr2))
        size=len(hashmap)    
        return sorted(arr1,key=lambda n:hashmap[n] if n in hashmap else size+n)