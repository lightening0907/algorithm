class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        log_list = []
        for log in logs:
            log = log.split(':')
            log_list.append((int(log[0]), log[1], int(log[2])))
        exclusive_times = [0]*n #store the exclusive time for function where id is
        log_list = sorted(log_list, key=lambda x: x[2]) # sort the time stamp
        len_logs = len(log_list)
        stack = []
        stack_accum = [] # get a accum for each begin
        for index_logs in range(len_logs):
            if log_list[index_logs][1] == 'start':
                stack.append(log_list[index_logs])
                stack_accum.append(0)
            elif log_list[index_logs][1] == 'end':
                start_f = stack.pop()
                cur_accum = stack_accum.pop()
                non_et = log_list[index_logs][2] - start_f[2]  + 1

                exclusive_times[log_list[index_logs][0]] += non_et - cur_accum
                if len(stack_accum) > 0:
                    stack_accum[-1] += non_et
        return exclusive_times