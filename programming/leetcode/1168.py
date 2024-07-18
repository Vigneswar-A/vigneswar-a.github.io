class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        flag=0
        for i in range(size:=len(arr)-1):
            if flag:
                flag-=1
                continue
            if arr[i]==0:
                arr[i:]=[0]+arr[i:size]
                flag+=1
        
        
        