class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        
        Students=dict()
        
        for Id,Mark in items:
            if Id not in Students:
                Students[Id]=[Mark]
            else:
                Students[Id].append(Mark)
                
        Result=[]
        
        for i in Students.items():
            Result.append((i[0],sum(sorted(i[1],reverse=1)[:5])//5))
            
        return sorted(Result,key=lambda a:a[0])
        