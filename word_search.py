"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell,
where "adjacent" cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once.
"""
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board and word: return False
        if not board: return True
        self.m = len(board)
        self.n = len(board[0])
        self.board = board
        # self.traveled = {}
        self.word = word
        self.len_word = len(word)
        for i in range(self.m):
            for j in range(self.n):
                if self.find_string(i,j,0): return True
        return False
    def find_string(self,i,j,w):
        if w>len(self.word)-1: return True
        if i>self.m-1 or i<0 or j>self.n-1 or j<0  or self.board[i][j] != self.word[w]:return False
        temp = self.board[i][j]
        self.board[i][j]= '#'
        if self.find_string(i+1,j,w+1): return True
        if self.find_string(i-1,j,w+1): return True
        if self.find_string(i,j+1,w+1): return True
        if self.find_string(i,j-1,w+1): return True
        self.board[i][j] = temp
        return False

class Solution2(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board and word:
            return False
        if not board:
            return True
        m = len(board)
        n = len(board[0])
        len_word = len(word)
        for i in range(m):
            for j in range(n):
                traveled_ij_dict = {0:[[i, j]]}
                temp_path = {}
                w_index = 0
                while traveled_ij_dict and w_index>=0:

                    if not traveled_ij_dict[w_index]:
                        del traveled_ij_dict[w_index]
                        w_index -= 1

                    else:
                        i_index = traveled_ij_dict[w_index][-1][0]
                        j_index = traveled_ij_dict[w_index][-1][1]

                        if board[i_index][j_index] != word[w_index]:
                            del traveled_ij_dict[w_index][-1]
                        else:
                            if w_index == len_word - 1: return True
                            if (i_index,j_index) in temp_path:
                                del temp_path[(i_index,j_index)]
                                del traveled_ij_dict[w_index][-1]
                                continue

                            temp_path[(i_index,j_index)] = 0
                            temp_travel = []
                            if i_index - 1 >= 0 and (i_index-1,j_index) not in temp_path:
                                temp_travel.append([i_index-1,j_index])
                            if i_index + 1 < m and (i_index+1,j_index) not in temp_path:
                                temp_travel.append([i_index+1,j_index])
                            if j_index - 1 >= 0 and (i_index,j_index-1) not in temp_path:
                                temp_travel.append([i_index,j_index-1])
                            if j_index + 1 < n and (i_index,j_index+1) not in temp_path:
                                temp_travel.append([i_index,j_index+1])
                            if w_index+1<len_word and temp_travel:
                                w_index +=1
                                traveled_ij_dict[w_index]=traveled_ij_dict.get(w_index,[]) + temp_travel

        return False

class Solution3(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        num_row = len(board)
        if not num_row:
            return False
        num_col = len(board[0])
        len_word = len(word)
        for row_index in range(num_row):
            for col_index in range(num_col):
                visited_word = {}
                len_visited_word = 0
                tb_visited = [(row_index, col_index)]
                while len(tb_visited) > 0:
                    ele_tb = tb_visited[-1]
                    if (ele_tb[0], ele_tb[1]) in visited_word:
                        del tb_visited[-1]
                        del visited_word[(ele_tb[0], ele_tb[1])]
                        len_visited_word -= 1
                    elif board[ele_tb[0]][ele_tb[1]] == word[len_visited_word]:
                        len_visited_word += 1
                        visited_word[(ele_tb[0],ele_tb[1])]=1
                        if ele_tb[0] - 1 >= 0 and (ele_tb[0] - 1,ele_tb[1]) not in visited_word:
                            tb_visited.append((ele_tb[0] - 1,ele_tb[1]))
                        if ele_tb[1] - 1 >= 0 and (ele_tb[0],ele_tb[1] - 1) not in visited_word:
                            tb_visited.append((ele_tb[0],ele_tb[1] - 1))
                        if ele_tb[0] + 1 < num_row and (ele_tb[0] + 1, ele_tb[1]) not in visited_word:
                            tb_visited.append((ele_tb[0] + 1, ele_tb[1]))
                        if ele_tb[1] + 1 < num_col and (ele_tb[0], ele_tb[1] + 1) not in visited_word:
                            tb_visited.append((ele_tb[0], ele_tb[1] + 1))
                    else:
                        del tb_visited[-1]
                    if len_visited_word == len_word:
                        return True
        return False
Solution1 = Solution3()
# print Solution1.exist(["ABCE","SFCS","ADEE"],"ABCCED")
print Solution1.exist([["a","b"]], "ba")