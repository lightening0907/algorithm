"""
443. String Compression
DescriptionHintsSubmissionsDiscussSolution
Given an array of characters, compress it in-place.

The length after compression must always be smaller than or equal to the original array.

Every element of the array should be a character (not int) of length 1.

After you are done modifying the input array in-place, return the new length of the array.


Follow up:
Could you solve it using only O(1) extra space?


Example 1:
Input:
["a","a","b","b","c","c","c"]

Output:
Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]

Explanation:
"aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".
Example 2:
Input:
["a"]

Output:
Return 1, and the first 1 characters of the input array should be: ["a"]

Explanation:
Nothing is replaced.
Example 3:
Input:
["a","b","b","b","b","b","b","b","b","b","b","b","b"]

Output:
Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].

Explanation:
Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb" is replaced by "b12".
Notice each digit has it's own entry in the array.
Note:
All characters have an ASCII value in [35, 126].
1 <= len(chars) <= 1000.
"""

class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        tot_len = 0
        len_char = 0
        index_char = 0
        len_chars = len(chars)
        while index_char < len_chars:
            if index_char == 0:
                len_char += 1
                index_char += 1
                tot_len += 1
            elif chars[index_char] == chars[index_char - 1]:
                len_char += 1
                del chars[index_char]

            elif chars[index_char] != chars[index_char - 1]:
                if len_char > 1:
                    chars = chars[:index_char] + list(str(len_char)) + chars[index_char:]
                    index_char = index_char + len(str(len_char)) + 1
                    tot_len += len(str(len_char))
                else:
                    index_char += 1
                len_char = 1
                tot_len += 1
            len_chars = len(chars)

        if len_char > 1:
            chars = chars + list(str(len_char))
            tot_len += len(str(len_char))
        print chars
        return tot_len

class Solution2(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if not chars:
            return 0
        elif len(chars) == 1:
            return 1

        cn = 1
        res = ''
        for i in range(1, len(chars)):
            if chars[i] == chars[i-1]:
                cn += 1
            else:
                res += chars[i-1] if cn == 1 else  chars[i-1] + str(cn)
                cn = 1

            if i == len(chars) - 1:
                res += chars[i] if cn == 1 else  chars[i] + str(cn)

        chars[:len(res)] = list(res)
        #chars = list(res) + chars[len(res): len(chars)]

        print(res)
        print(chars)
        #print(len(res))
        return len(res)
print Solution().compress(["a","a","a","a","b","b","b","b","b","b","b","c","c"])