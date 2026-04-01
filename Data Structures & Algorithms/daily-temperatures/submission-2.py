class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #brute force -- for each element, run a while loop and use a counter to count
        #how many days until a warmer temp is found, time complexity 
        res = []
        for i in range(len(temperatures)):
            days = 1
            j = i+1
            foundGreater = False
            while j < len(temperatures):
                print(temperatures[i], temperatures[j])
                if temperatures[j] > temperatures[i]:
                    res.append(days)
                    foundGreater = True
                    break
                days += 1
                j += 1
            if not foundGreater:
                res.append(0)

        return res
            