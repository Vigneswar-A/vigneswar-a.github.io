class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        rest_a = {s : i for i , s in enumerate(list1)}
        rest_b = {s : i for i , s in enumerate(list2)}
        
        res = []
        minindex = float('inf')
        for rest in set(list1).intersection(set(list2)):
            temp = rest_a[rest] + rest_b[rest]
            if temp < minindex:
                res.clear()
                res.append(rest)
                minindex = temp
            elif temp == minindex:
                res.append(rest)
                    
        return res
                
        
        