class Solution:
    def DSU(self):
        root = {}

        def findRoot(x):
            if root[x] != x:
                root[x] = findRoot(root[x])
            return root[x]
        
        def union(x, y):
            x = findRoot(x)
            y = findRoot(y)
            if x < y:
                root[y] = x
            else:
                root[x] = y