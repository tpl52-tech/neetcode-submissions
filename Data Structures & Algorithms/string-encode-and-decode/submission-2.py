class Solution:

    def encode(self, strs: List[str]) -> str:

        res = []

        for elem in strs: 
            res.append(str(len(elem)))
            res.append(',')
        
        res.append('#')
        res.extend(strs)
        res = "".join(res)

        return res
        

    def decode(self, s: str) -> List[str]:

        sizes, res = [], []
        i = 0

        while s[i] != '#':
            j = i 
            while s[j] != ',':
                j += 1
            sizes.append(int(s[i:j]))
            i = j + 1
        
        for sz in sizes: 
            res.append(s[i:j])
            i = j + 1
        
        return res

        





