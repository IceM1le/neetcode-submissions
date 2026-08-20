class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): return -1
        n = len(gas)
        fuel = 0
        ind = 0
        for i in range(n):
            fuel += gas[i] - cost[i]
            if fuel < 0:
                fuel = 0
                ind = i + 1
        return ind