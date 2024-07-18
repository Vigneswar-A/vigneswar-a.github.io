class Solution:
    def minimumCosts(self, regular: List[int], express: List[int], expressCost: int) -> List[int]:
        
        @cache
        def dp(node):
            if node == 1:
                return 0
            if node == -1:
                return expressCost
            if node < 0:
                return min(
                    dp(node+1)+express[-node-2],
                    dp(-node-1)+expressCost+regular[-node-2]
                )
                
            else:
                return min(
                    dp(node-1)+regular[node-2],
                    dp(-node+1)+express[node-2]
                )

        return [dp(i) for i in range(2, len(regular)+2)]