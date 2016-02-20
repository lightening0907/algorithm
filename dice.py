__author__ = 'ChiYuan'
import random
class dice:
    def __init__(self,prob=[],side=6,d_bias = False):

        self.side = side
        self.d_bias = d_bias
        if prob:
            self.prob = prob
            self.side = len(prob)
        elif self.d_bias==0:
            self.prob = [1/side for x in range(side)]

    def roll(self,N):

        result = []
        for rep in range(N):
            rand_roll = random.random()
            accu_prob = self.prob[0]
            for i in range(self.side):
                if accu_prob<rand_roll:
                    accu_prob += self.prob[i+1]
                else:
                    result.append(i+1)
                    break
        print(result)
        return result

dice1 = dice(prob=[0.1,0.5,0.4,0,0],d_bias=True)
dice1.roll(20)





