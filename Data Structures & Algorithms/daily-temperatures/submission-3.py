class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #use a stack, for each temp, while temp at the top of the
        #stack < current, pop and added the difference to the 
        #corresponding index 
        stack = []
        res = [0] * len(temperatures)
        print(res)
        #38, 
        for i in range(len(temperatures)):
            while stack and stack[len(stack)-1][0] < temperatures[i]:
                top, idx = stack.pop()
                res[idx] = i - idx
            stack.append((temperatures[i], i))

        return res

            