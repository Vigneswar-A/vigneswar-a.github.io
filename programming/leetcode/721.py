class UnionFind:
    def __init__(self , n):
        self.root = [*range(n)]
        self.rank = [1] * n
        
    def find(self , x):
        if x == self.root[x]:
            return x
        x = self.root[x] = self.find(self.root[x])
        return x
    
    def union(self , x, y):
        x = self.find(x)
        y = self.find(y)
        
        if x == y:
            return False
        
        if self.rank[x] > self.rank[y]:
            self.root[y] = x
        elif self.rank[x] < self.rank[y]:
            self.root[x] = y
        else:
            self.rank[x] += 1
            self.root[y] = x
            
        return True
    
    def is_connected(self, x, y):
        return self.find(x) == self.find(y)

    def clean(self):
        for i in range(len(self.root)):
            self.root[i] = self.find(self.root[i])
        return self.root


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        uf = UnionFind(n)

        for i in range(n):
            for j in range(i+1, n):
                if accounts[i][0] == accounts[j][0] and any(account in accounts[j][1:] for account in accounts[i][1:]):
                    uf.union(i, j)

        mails = defaultdict(list)
        groups = uf.clean()

        for id,mail in zip(groups, accounts):
            mails[(id, mail[0])].extend(mail[1:])

        res = []
        for (id,name),mail in mails.items():
            res.append([name, *sorted(set(mail))])
        
        return res

        