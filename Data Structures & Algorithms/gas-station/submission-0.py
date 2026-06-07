class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        curr_gas = 0
        start = 0
        gas_sum = 0
        cost_sum = 0

        for i in range(len(gas)):
            curr_gas += gas[i] - cost[i]
            gas_sum += gas[i]
            cost_sum += cost[i]
            if curr_gas < 0:
                start = i + 1
                curr_gas = 0
        
        if gas_sum < cost_sum:
            return -1
        
        return start
                
