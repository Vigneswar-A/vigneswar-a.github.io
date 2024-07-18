class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        out_degree = defaultdict(list)
        pre_req = {}
        
        for recepie,ingredient in zip(recipes, ingredients):
            pre_req[recepie] = len(ingredient)
            for ing in ingredient:
                out_degree[ing].append(recepie)
                if ing not in pre_req:
                    pre_req[ing] = 0      
           
        supplies = set(supplies)
        queue = deque([item for item,req in pre_req.items() if req == 0 and item in supplies])
        menu = set()
        while queue:
            item = queue.popleft()
            
            for recepie in out_degree[item]:
                pre_req[recepie] -= 1
                if pre_req[recepie] == 0:
                    menu.add(recepie)
                    queue.append(recepie)
        
        return menu
            
            
                    
        
    