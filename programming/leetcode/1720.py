class Solution:
    def minOperations(self, logs: List[str]) -> int:
        
        layer = 0
        for log in logs:
            if log == "../" and layer:
                layer -= 1
            elif log == "./":
                continue
            elif log != "../":
                layer += 1
                
        return layer
                