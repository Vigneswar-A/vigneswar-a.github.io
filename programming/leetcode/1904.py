class Solution:
    def secondHighest(self, s: str) -> int:
        arr=[]
        [arr.append(int(i)) for i in s if i.isdigit() and int(i) not in arr]
        if len(sorted(arr))>1:
            return sorted(arr)[-2]
        else:
            return -1
        
        