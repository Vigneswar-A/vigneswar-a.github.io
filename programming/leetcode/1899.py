class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        
        class Item:
            def __init__(self, args):
                type, color, name = args
                self.type = type
                self.color = color
                self.name = name
                
                
        items = [*map(Item, items)]
        
        count = 0
        for item in items:
            if item.__dict__[ruleKey] == ruleValue:
                count += 1
                
        return count