class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        while curr temp > top of stack:
            take diff and update outputArray[topstackIdx] with currIdx - topstackIdx
        otherwise, append curr temp to the stack, (temp,idx)
        """
        res = [0] * len(temperatures)
        s = []
        for i in range(len(temperatures)):
            while len(s) and temperatures[i] > s[-1][0]:
                _,idx = s.pop()
                res[idx] = i - idx
            s.append((temperatures[i],i))
        
        return res