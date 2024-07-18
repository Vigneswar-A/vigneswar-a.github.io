"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children
"""

class Codec:
    def serialize(self, root: 'Node') -> str:
        if not root:
            return ''
        if not root.children:
            return "("+str(root.val)+")"
        return str(root.val) + "(" + "".join(self.serialize(child) for child in root.children) + ")"
        
    def deserialize(self, data: str) -> 'Node':
        if not data:
            return None
        if data[0] == '(':
            return Node(int(data[1:-1]))
        
        root_val, _, child = data[:-1].partition('(')
        root = Node(int(root_val))     
        temp = ''
        count = 0
        for c in child:
            temp += c
            if c == '(':
                count += 1
            elif c == ')':
                count -= 1
                if count == 0:
                    root.children.append(self.deserialize(temp))
                    temp = ''
        return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))