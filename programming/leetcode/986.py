class Hashable_Counter(Counter):
    def __hash__(self):
        return hash(tuple(sorted(self.items())))
    
res = {}

for i in range(24):
    for j in range(60):
        temp = Hashable_Counter(map(int , ('0' if i < 10 else '')+str(i)+('0' if j  and j < 10 else '')+str(j)+('0' if not j else '')))     
        res[temp] = max(f"{0 if i < 10 else ''}{i}:{0 if j and j < 10 else ''}{j}{0 if not j else ''}" , res.get(temp , ''))
        
class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        return res.get(Hashable_Counter(arr),'')
        