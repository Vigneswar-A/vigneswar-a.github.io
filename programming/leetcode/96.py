class Solution(object):
    def numTrees(self, n):
        return functools.reduce(lambda n , i : n * 2*(2*i+1)//(i+2) , range(0 , n) , 1)
