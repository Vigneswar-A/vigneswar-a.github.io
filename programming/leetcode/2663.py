class Solution:
    def distMoney(self, money: int, children: int) -> int:
        
        max_childs, rem = divmod(money-children, 7)
        if max_childs < 0:
            return -1
        elif max_childs > children:
            return children - 1
        elif max_childs == children:
            return children if rem == 0 else children - 1
        elif max_childs == children-1 and rem == 3:
            return max_childs - 1
        else:
            return max_childs