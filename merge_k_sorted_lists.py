# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return None
        sorted_list = sorted( [tmp for tmp in lists if tmp], key= lambda x: x.val) # place holder for future nodes that are not directly connected
        if len(sorted_list) == 0:
            return None
        return_node = sorted_list.pop(0)
        smallest_node = return_node
        while len(sorted_list)>0:
            if not smallest_node.next:
                smallest_node.next = sorted_list[0]
            elif sorted_list[0].val < smallest_node.next.val:
                left = 0
                right = len(sorted_list) -1
                if smallest_node.next.val >= sorted_list[right].val:
                    sorted_list.append(smallest_node.next)
                else:
                    res = None
                    while right - left > 1:
                        mid = (right + left) //2
                        if sorted_list[mid].val < smallest_node.next.val:
                            left = mid
                        elif sorted_list[mid].val > smallest_node.next.val:
                            right = mid
                        else:
                            res = mid
                            break

                    if not res:
                        res=left
                    sorted_list = sorted_list[:res+1] + [smallest_node.next] + sorted_list[res+1:]
                smallest_node.next = sorted_list[0]
            elif sorted_list[0].val >= smallest_node.next.val:
                sorted_list.insert(0, smallest_node.next)
            if len(sorted_list)>0:
                smallest_node = sorted_list.pop(0)
        return return_node

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

list_lists = [[-8,-7,-7,-5,1,1,3,4],[-2],[-10,-10,-7,0,1,3],[2]]
list_nodes = []
for i in range(len(list_lists)):
    for j in range(len(list_lists[i])):
        if j == 0:
            nodehead = ListNode(list_lists[i][j])
            list_nodes.append(nodehead)
        else:
            nodehead.next = ListNode(list_lists[i][j])
            nodehead = nodehead.next

solution = Solution()
res = solution.mergeKLists(list_nodes)
while res:
    print res.val
    res = res.next
