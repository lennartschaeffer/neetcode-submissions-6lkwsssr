class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        #to encode, use (length, delimiter, word)
        for s in strs:
            res.append(str(len(s)))
            res.append('#')
            res.append(s)

        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        
        res = []

        i = 0

        # 4#neet4#code4#love3#you
        # 
        
        while i < len(s):
            j = i
            #get the length of the word
            while s[j] != '#':
                j += 1
            print(s[i:j])
            length = int(s[i:j])
            #get the word
            i = j + 1 #move lower pointer ahead of the delimiter
            j += length #move upper pointer ahead by length characters
            res.append(s[i:j+1])
            i = j + 1 #update the lower pointer

        return res


        
        