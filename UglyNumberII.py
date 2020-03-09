class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        dict_ugly = {}
        pr_list = [2,3,5]
        for i in pr_list:
            dict_ugly[i]=[1]
        #visited_ugly = {1:1}
        if n ==1:
            return 1
        i=2
        while True:
            min_candidate = min(dict_ugly[2][0]*2, dict_ugly[3][0]*3, dict_ugly[5][0]*5)
            #if min_candidate in visited_ugly:
            #    continue
            for pr in pr_list:
                if dict_ugly[pr][0]*pr==min_candidate:
                    del dict_ugly[pr][0]
                    #break
                dict_ugly[pr].append(min_candidate)
            if i == n: return min_candidate
            i+=1

Solution1 = Solution()
print Solution1.nthUglyNumber(10)

class Solution2(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        traversed_dict = {} # {visited_number: index}
        list_primes = [2, 3, 5]
        current_ugly = 1
        tb_visited_list = []
        index = 1
        while index < n:
            if len(tb_visited_list) == 0:
                tb_visited_list = [current_ugly*prime for prime in list_primes]
            if tb_visited_list[0] not in traversed_dict:
                traversed_dict[tb_visited_list[0]] = index
                index += 1
                current_ugly = tb_visited_list[0]
            new_candidate = [tb_visited_list[0]*prime for prime in list_primes]
            tb_visited_list = tb_visited_list[1:]
            insert_i = 0
            # print tb_visited_list, new_candidate
            for candidate in new_candidate:
                # print candidate, insert_i, tb_visited_list, tb_visited_list[insert_i]
                while insert_i <= len(tb_visited_list)-1 and candidate > tb_visited_list[insert_i]:
                    insert_i += 1
                # print insert_i, candidate
                if insert_i == len(tb_visited_list) or candidate < tb_visited_list[insert_i]:
                    tb_visited_list.insert(insert_i, candidate)
                    # print tb_visited_list
                    insert_i += 1
            # print tb_visited_list
        return current_ugly

class Solution3(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        traversed_dict = {} # {visited_number: index}
        list_primes = [2, 3, 5]
        current_ugly = 1
        tb_visited_list = []
        heapq.heappush(tb_visited_list, 1)
        index = 0
        min_num = 0
        while index < n:
            while tb_visited_list and tb_visited_list[0] <= min_num:
                heapq.heappop(tb_visited_list)
            min_num = heapq.heappop(tb_visited_list)
            for prime in list_primes:
                heapq.heappush(tb_visited_list, min_num*prime)
            if min_num not in traversed_dict:
                traversed_dict[min_num] = index
                index += 1
        return min_num