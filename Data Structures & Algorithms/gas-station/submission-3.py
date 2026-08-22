class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): return -1
        ind = 0
        tank = 0
        n = len(gas)
        for i in range(n):
            tank += gas[i]
            if tank >= cost[i]:
                tank -= cost[i]                
            else:
                tank = 0
                ind = i + 1
        return ind