class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        len_gas = len(gas)
        candidate = [0]
        net = []
        accum_sum = []

        part_sum = None
        for i in range(len_gas):
            net.append(gas[i]-cost[i])
            if net[-1]>0 and (len(net)>1 and net[-2]<0) and (part_sum<0):
                candidate.append(i)
                accum_sum.append(part_sum)
                part_sum = net[-1]
            else:
                if not part_sum: part_sum = net[-1]
                else: part_sum += net[-1]
        accum_sum.append(part_sum)
        if sum(accum_sum)<0: return -1
        else:
            max_v = accum_sum[0]
            max_index = candidate[0]
            for i in range(len(accum_sum)):
                if accum_sum[i]>max_v:
                    max_v = accum_sum[i]
                    max_index = candidate[i]
        return max_index

class Solution2(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        len_gas = len(gas)
        candidate = [0]
        net = []
        accum_sum = []
        tot_sum = 0

        part_sum = None
        max_index = -1
        max_value = 0
        for i in range(len_gas):
            net.append(gas[i]-cost[i])
            if net[-1]>0 and (len(net)>1 and net[-2]<0) and (part_sum<0):
                candidate.append(i)
                accum_sum.append(part_sum)
                if part_sum > max_value:
                    max_value=part_sum
                    max_index = candidate[-2]
                tot_sum += part_sum
                part_sum = net[-1]
            else:
                if not part_sum: part_sum = net[-1]
                else: part_sum += net[-1]
        accum_sum.append(part_sum)
        if part_sum >= max_value:
            max_value=part_sum
            max_index = candidate[-1]
        tot_sum += part_sum
        if tot_sum<0: return -1
        return max_index
Solution1 = Solution2()
print Solution1.canCompleteCircuit([2],[2])