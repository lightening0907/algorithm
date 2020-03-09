# -*- coding: utf-8 -*-
"""
* 有weight的随机
    * Given two vectors, one with a set of values, and one with a set of weights, write a function that will randomly sample a single value from the values vector with weight given in the weight vector.
        * For example:
        * Values   <- c(3, 17, 23, 0, 1, 8, 5.2)
        * Weights <- c(9, 3, 33, 0.5, 3, 8, 1)
        * In this example, the value ‘23’ would be 11 times more likely to be sampled than the value ‘17’ because it’s weight is 11 times larger (33 vs. 3)
    * 上来就让你自己写weighted sampling, 不能用existing function。 给两个vector, 一个是要选的数，另一个是相应的weight。 我说根据相应的weight来replicate选择的数，再用一个uniform distribution来随即选index。白人哥哥但是这样会有个问题，我说是阿，如果weight是小数的话就有问题，可以试着把weight vector整体乘一个很大的数，变成整数之类的。。。
"""
import numpy as np
class WeightedSampling(object):
    def __init__(self, weights, values):
        # turn weights into boundaries for bins of uniform random numbers between 0 and 1
        # that map into each number in the sample
        self.values = values
        tot_weights = sum(weights)
        self.bound_randnum = [weight*1.0/tot_weights for weight in weights]
        self.len_sample = len(values)
        for i in range(self.len_sample):
            if i > 0:
                self.bound_randnum[i] += self.bound_randnum[i-1]

    def sample(self,n):
        # sample with replacement for N number
        sampled_val = []
        print self.bound_randnum
        for i_s in range(n):
            unit_rn = np.random.uniform(size=1)
            # use binary search to find the bin that this random number fall into
            # and the corresponding number at that location in array of values is the sample we have
            l_index = 0
            r_index = self.len_sample - 1
            if self.bound_randnum[0] >= unit_rn:
                sampled_val.append(self.values[0])
                print i_s,'random number', unit_rn, 'sampled_bin', self.bound_randnum, 'sampled_values',0
                continue
            while r_index - l_index > 1:
                mid_index = (l_index + r_index)/2
                if self.bound_randnum[mid_index] == unit_rn:
                    sampled_val.append(self.values[mid_index])
                    print i_s,'random number', unit_rn, 'sampled_bin', self.bound_randnum, 'sampled_values', mid_index
                    break
                elif self.bound_randnum[mid_index] < unit_rn:
                    l_index = mid_index
                elif self.bound_randnum[mid_index] > unit_rn:
                    r_index = mid_index
            sampled_val.append(self.values[r_index])
            print i_s,'random number', unit_rn, 'sampled_bin', self.bound_randnum, 'sampled_index', r_index
        return sampled_val

values = [3, 17, 23, 0, 1, 8, 5.2]
weights = [9, 3, 1, 0.5, 3, 8, 1]
print WeightedSampling(weights, values).sample(10)


