"""
721. Accounts Merge
https://leetcode.com/problems/accounts-merge/
Given a list accounts, each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some email that is common to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

Example 1:
Input:
accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
Output: [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
Explanation:
The first and third John's are the same person as they have the common email "johnsmith@mail.com".
The second John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'],
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
Note:

The length of accounts will be in the range [1, 1000].
The length of accounts[i] will be in the range [1, 10].
The length of accounts[i][j] will be in the range [1, 30].
"""


class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        accounts = sorted(accounts, key=lambda x: x[0])
        merged_accounts = []
        merged_ct = {} # name: user count, how many unique users there are under each name
        for i, account in enumerate(accounts):
            sorted_account = sorted(account[1:])
            tmp_account = []
            for ac_index, ac_val in enumerate(sorted_account):
                if ac_index == 0:
                    tmp_account.append(ac_val)
                elif ac_val != sorted_account[ac_index - 1]:
                    tmp_account.append(ac_val)
            account = [account[0]] + tmp_account
            if i == 0 or account[0]!=merged_accounts[-1][0]:
                merged_accounts.append(account)
                merged_ct[account[0]] = 1
            else:
                unique_users = merged_ct[account[0]] #number of users to compare with
                len_account = len(account)
                for j in range(-1, -1 - unique_users, -1):
                    over_lap_flag = False
                    tmp_list_account = merged_accounts[j][1:]
                    email_index_2_init = 0
                    for email_index_1, email_1 in enumerate(account[1:]):
                        len_tmp_list_account = len(tmp_list_account)
                        for email_index_2 in range(email_index_2_init, len_tmp_list_account):
                            email_2 = tmp_list_account[email_index_2]
                            if email_index_2 == 0 and email_1 < email_2:
                                tmp_list_account.insert(0, email_1)
                                email_index_2_init = email_index_2
                                break
                            elif email_1 > tmp_list_account[email_index_2 - 1] and email_1 < email_2:
                                tmp_list_account.insert(email_index_2, email_1)
                                email_index_2_init = email_index_2
                                break
                            elif email_1 > email_2 and email_index_2 == len(tmp_list_account) - 1:
                                tmp_list_account.append(email_1)
                                email_index_2_init = email_index_2
                                break
                            elif email_1 == email_2:
                                over_lap_flag = True
                                email_index_2_init = email_index_2
                                break
                            email_index_2 += 1
                    if over_lap_flag:
                        merged_accounts[j] = [account[0]] + tmp_list_account
                        break
                if not over_lap_flag:
                    merged_accounts.append(account)
                    merged_ct[account[0]] += 1
        return merged_accounts


import collections
class UF(object):
    def __init__(self):
        self.uf_list = list(range(10001))

    def find_root(self, x):
        while self.uf_list[x] != x:
            x = self.find_root(self.uf_list[x])
        return x

    def union(self, x, y):
        self.uf_list[self.find_root(y)] = self.find_root(x)

class Solution2(object):
    def accountsMerge(self, accounts):
        uf = UF()
        email_to_name = {}
        email_to_id = {}
        id_to_email = {}
        i = 0
        for account in accounts:
            for acc_index, acc in enumerate(account):
                if acc_index >= 1:
                    if acc not in email_to_id:
                        email_to_id[acc] = i
                        id_to_email[i] = acc
                        i += 1
                    email_to_name[acc] =  account[0]
                    uf.union(email_to_id[account[1]], email_to_id[acc])

        unique_users = collections.defaultdict(list)
        for ele in email_to_name:
            unique_users[id_to_email[uf.find_root(email_to_id[ele])]].append(ele)
        ans = []
        for ele in unique_users:
            ans.append([email_to_name[ele]] + sorted(unique_users[ele]))
        return ans
solution = Solution2()
print(solution.accountsMerge([["David","David0@m.co","David4@m.co","David3@m.co"],["David","David5@m.co","David5@m.co","David0@m.co"],["David","David1@m.co","David4@m.co","David0@m.co"],["David","David0@m.co","David1@m.co","David3@m.co"],["David","David4@m.co","David1@m.co","David3@m.co"]]))