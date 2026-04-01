class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # brute force, is try each station, simulate the process, and keep track of if
        # its possible

        res = -1


        for i in range(len(gas)):
            currGas = 0
            currStation = i
            loop = False
            while currGas >= 0:
                if currStation > len(gas)-1:
                    currStation = 0
                    loop = True
                if loop and currStation == i:
                    res = currStation
                    break
                currGas += gas[currStation]
                currGas -= cost[currStation]
                currStation += 1


        return res