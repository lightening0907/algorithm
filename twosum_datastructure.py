__author__ = 'ChiYuan'
class TwoSum:

    # initialize your data structure here
    def __init__(self):
        self.numl = {}
        self.suml = {}


    # @return nothing
    def add(self, number):
        if number not in self.numl:
            print(self.numl)
            if not self.numl:
                self.numl[number] = 1
                print(self.numl)
            else:
                for en in self.numl:
                    print(en)
                    if number+en not in self.suml:
                        self.suml[number+en]=1

                self.numl[number] = 1
                print(self.suml)
        else:
            if 2*number not in self.suml:
                self.suml[2*number] = 1
    # @param value, an integer
    # @return a Boolean
    def find(self, value):
        if value in self.suml:
            return True
        else:
            return False

ts=TwoSum()
print(ts.find(0))
print(ts.add(1))
print(ts.add(3))
#print(TwoSum().add(5))
print(ts.find(4))
