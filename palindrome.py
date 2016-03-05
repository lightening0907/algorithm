# Determine whether an integer is a palindrome. Do this without extra space.
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x< 0 : return False
        l_x = 1
        while x//(10**l_x)>0:
            l_x += 1
        #print(l_x)
        while l_x>0:
            if l_x == 1 : return True
            elif x%10 == x//(10**(l_x-1)): # compare the digit at two end, if being the same, truncate both of them
                x = (x%(10**(l_x-1)))//10
                l_x = l_x -2 # length minus 2
               #print(x,l_x)
            else: return False
        return True